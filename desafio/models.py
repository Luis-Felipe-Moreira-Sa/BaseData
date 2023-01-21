from django.db import models
from django.conf import settings


# Create your models here.

class Cliente(models.Model):
    id_codigo = models.IntegerField(verbose_name="Codigo", unique=True)
    nome = models.CharField(verbose_name="Nome", max_length=200)
    sobrenome = models.CharField(verbose_name="Sobrenome", max_length=200)
    sexo = models.CharField(verbose_name="Sexo", max_length=20)
    altura = models.IntegerField(verbose_name="Altura")
    peso = models.FloatField(verbose_name="Peso")
    nascimento = models.DateField(verbose_name="Nascimento")
    bairro = models.CharField(verbose_name="Bairro", max_length=200)
    cidade = models.CharField(verbose_name="Cidade", max_length=200)
    estado = models.CharField(verbose_name="Estado", max_length=200)
    numero = models.IntegerField(verbose_name="Numero")
    # descricao = models.TextField()


    def __str__(self):
        return self.nome
        # return self.id_codigo, self.nome, self.sobrenome, self.sexo, self.altura, self.peso, self.nascimento, self.bairro, self.cidade, self.estado, self.numero
