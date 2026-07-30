from django.db import models

# Create your models here.
class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    lider = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()
    qtde_membros = models.IntegerField()
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome