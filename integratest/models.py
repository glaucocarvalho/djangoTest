from django.db import models


class Data(models.Model):
    id_cli = models.IntegerField()
    ponto = models.IntegerField()
    nome_cli = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    lat = models.CharField(max_length=200, default =0)
    lon = models.CharField(max_length=200, default =0)

class Dados(models.Model):
    id_cli = models.IntegerField(blank=True, null=True)
    ponto = models.IntegerField(blank=True, null=True)
    nome_cli = models.CharField(max_length=45, blank=True, null=True)
    endereco = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dados'

