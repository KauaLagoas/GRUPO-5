from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Mensagem

class ChatTests(TestCase):
    def setUp(self):
        self.a, self.b, self.c = [get_user_model().objects.create_user(username=n, password="senha-teste-123") for n in ("ana", "bruno", "carla")]
        self.url = reverse("chat:conversa", args=[self.b.pk])
    def test_login_obrigatorio(self):
        self.assertEqual(self.client.get(self.url).status_code, 302)
    def test_envio_e_persistencia(self):
        self.client.force_login(self.a)
        self.client.post(self.url, {"texto":"Olá!", "remetente":self.c.pk})
        m = Mensagem.objects.get()
        self.assertEqual((m.remetente, m.destinatario, m.texto), (self.a, self.b, "Olá!"))
        self.client.force_login(self.b)
        self.assertContains(self.client.get(reverse("chat:conversa", args=[self.a.pk])), "Olá!")
    def test_privacidade(self):
        Mensagem.objects.create(remetente=self.c, destinatario=self.b, texto="segredo-terceiro")
        self.client.force_login(self.a)
        self.assertNotContains(self.client.get(self.url), "segredo-terceiro")
    def test_validacao(self):
        self.client.force_login(self.a)
        for texto in ("   ", "x"*2001):
            self.assertEqual(self.client.post(self.url, {"texto":texto}).status_code, 200)
        self.assertFalse(Mensagem.objects.exists())
        self.assertEqual(self.client.get(reverse("chat:conversa", args=[self.a.pk])).status_code,404)
        self.assertEqual(self.client.get(reverse("chat:conversa", args=[999999])).status_code,404)
    def test_csrf(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.a)
        self.assertEqual(client.post(self.url, {"texto":"teste"}).status_code, 403)
    def test_escape_html(self):
        Mensagem.objects.create(remetente=self.b, destinatario=self.a, texto="<script>alert(1)</script>")
        self.client.force_login(self.a)
        response = self.client.get(self.url)
        self.assertContains(response, "&lt;script&gt;")
        self.assertNotContains(response, "<script>")
