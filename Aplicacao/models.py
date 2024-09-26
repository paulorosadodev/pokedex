from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    tipo1 = models.CharField(max_length=50)
    tipo2 = models.CharField(max_length=50, blank=True, null=True)
    hp = models.IntegerField()
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    imagem = models.URLField(max_length=200)


