from django.db import models


# Esta classe vira uma TABELA no banco. Cada linha abaixo vira uma COLUNA.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=200)  # guarda a senha criptografada
    habilidadeEnsina = models.CharField(max_length=100)
    habilidadeAprende = models.CharField(max_length=100)

class Denuncia(models.Model):
    TIPO_CHOICES = [
        ('usuario', 'Usuário'),
        ('habilidade', 'Habilidade'),
    ]
    
    STATUS_CHOICES = [('aberta', 'Aberta'), ('em_analise', 'Em análise'), ('resolvida', 'Resolvida')]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    usuario_alvo = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='denuncias')
    habilidade_alvo = models.CharField(max_length=100, blank=True)

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    alvo = models.CharField(max_length=100)
    motivo = models.CharField(max_length=150)
    descricao = models.TextField()
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo.capitalize()}: {self.alvo}"

class EventoModeracao(models.Model):
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE, related_name='eventos')
    moderador = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)
    descricao = models.CharField(max_length=250)
    criado_em = models.DateTimeField(auto_now_add=True)
