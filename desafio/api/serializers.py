from django.db import models
from django.db.models import fields
from rest_framework import serializers
from desafio.models import Cliente
# from desafio import models


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id', 'id_codigo', 'nome', 'sobrenome',
            'sexo', 'altura', 'peso', 'nascimento',
            'bairro', 'cidade', 'estado', 'numero',
        ]


# class ClienteMereenSerializer(serializers.ModelSerializer):
