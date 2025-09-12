from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class ExcelPlanilha(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # <- usa o modelo customizado
        on_delete=models.CASCADE
    )
    permission = models.BigIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'planilhas'
