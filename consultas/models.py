# consultas/models.py
from django.db import models

class Consultas(models.Model):
    nome = models.CharField(max_length=100)
    consultas = models.CharField(max_length=120)
    area = models.CharField(max_length=100)
    permission = models.BigIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'consultas'
