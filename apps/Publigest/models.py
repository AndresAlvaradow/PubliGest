from django.db import models

class DataScrapy(models.Model):
    post_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=850, blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    loves = models.IntegerField(blank=True, null=True)
    hahas = models.IntegerField(blank=True, null=True)
    wows = models.IntegerField(blank=True, null=True)
    sads = models.IntegerField(blank=True, null=True)
    hates = models.IntegerField(blank=True, null=True)
    cares = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=800, blank=True, null=True)

class EntidadesNombradas(models.Model):
    ent_id = models.AutoField(primary_key=True)
    entidad = models.CharField(max_length=850, blank=True, null=True)
    etiqueta = models.CharField(max_length=10, blank=True, null=True)

class PalabrasClaves(models.Model):
    kw_id = models.AutoField(primary_key=True)
    keyswords = models.CharField(max_length=850, blank=True, null=True)
    text = models.CharField(max_length=850, blank=True, null=True)

class EntidadesNombradas_texto(models.Model):
    id_ent_text = models.AutoField(primary_key=True)
    entidad = models.CharField(max_length=850, blank=True, null=True)
    texto = models.CharField(max_length=850, blank=True, null=True)