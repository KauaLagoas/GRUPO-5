from django.contrib.auth.models import User
from django.test import TestCase

from .models import Usuario
from .recomendacoes import recomendar, normalizar


def criar(username, ensina, aprende):
    return Usuario.objects.create(
        nome=username.capitalize(), username=username, senha="x",
        habilidadeEnsina=ensina, habilidadeAprende=aprende,
    )


class RecomendacoesTest(TestCase):
    def test_normalizar_ignora_acento_e_caixa(self):
        self.assertEqual(normalizar("  INGLÊS "), "ingles")

    def test_troca_perfeita_vem_separada_e_sem_repetir(self):
        ana = criar("ana", "Programação", "Inglês")
        criar("bia", "ingles", "programacao")      # troca perfeita
        criar("caio", "Inglês", "Violão")          # só ensina o que Ana quer
        criar("duda", "Piano", "Programação")      # só quer o que Ana ensina
        criar("edu", "Piano", "Violão")            # nada em comum
        r = recomendar(ana)
        self.assertEqual([i["usuario"].username for i in r["troca_perfeita"]], ["bia"])
        self.assertEqual([i["usuario"].username for i in r["ensinam_voce"]], ["caio"])
        self.assertEqual([i["usuario"].username for i in r["aprendem_voce"]], ["duda"])

    def test_nunca_recomenda_a_si_mesmo(self):
        ana = criar("ana", "Python", "Python")
        r = recomendar(ana)
        self.assertEqual(sum(len(v) for v in r.values()), 0)

    def test_varias_habilidades_separadas_por_virgula(self):
        ana = criar("ana", "Python, Excel", "Inglês, Francês")
        criar("bia", "Francês", "Excel")
        r = recomendar(ana)
        self.assertEqual(len(r["troca_perfeita"]), 1)


class TelaRecomendacoesTest(TestCase):
    def test_exige_login(self):
        resposta = self.client.get("/recomendacoes/")
        self.assertEqual(resposta.status_code, 302)

    def test_mostra_recomendacao_para_usuario_logado(self):
        criar("ana", "Programação", "Inglês")
        criar("bia", "Inglês", "Programação")
        User.objects.create_user("ana", password="123")
        self.client.login(username="ana", password="123")
        resposta = self.client.get("/recomendacoes/")
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Troca perfeita")
        self.assertContains(resposta, "Bia")
