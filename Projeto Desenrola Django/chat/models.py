from django.conf import settings
from django.db import models
from django.db.models import F, Q

class Mensagem(models.Model):
    remetente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mensagens_enviadas")
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mensagens_recebidas")
    texto = models.TextField(max_length=2000)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["criada_em", "pk"]
        indexes = [models.Index(fields=["remetente", "destinatario", "criada_em"])]
        constraints = [models.CheckConstraint(condition=~Q(remetente=F("destinatario")), name="chat_pessoas_distintas")]
