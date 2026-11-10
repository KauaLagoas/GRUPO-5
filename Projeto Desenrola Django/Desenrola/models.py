from django.db import models
from django.contrib.auth.models import User

class Denuncia(models.Model):
    TIPO_CHOICES = [
        ('usuario', 'Usuário'),
        ('habilidade', 'Habilidade'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    alvo = models.CharField(max_length=100)
    motivo = models.CharField(max_length=150)
    descricao = models.TextField()
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo.capitalize()}: {self.alvo}"

class Usuario(models.Model):
    FORMATO_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Online', 'Online'),
        ('Flexível', 'Flexível'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bio = models.TextField(max_length=200)
    formato_troca = models.CharField(max_length=20, choices=FORMATO_CHOICES, default='Flexível')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Habilidade(models.Model):
    TIPO_CHOICES = [
        ('ensinar', 'Posso Ensinar'),
        ('aprender', 'Quero Aprender'),
    ]
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='habilidades')
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"