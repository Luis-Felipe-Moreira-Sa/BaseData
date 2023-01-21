from rest_framework import viewsets
from django.db import models
from desafio.models import Cliente
from desafio.api import serializers

from django.db.models.query import QuerySet
from desafio.admin import Clientes
from django.shortcuts import render


class DesafioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = Cliente.objects.all().filter(cidade='Meeren', sexo='F')
    # authentication_classes = [BaseAuthentication]
    # permission_classes = [IsAuthenticated]


class MaleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = Cliente.objects.all().filter(sexo='M')


class FemaleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = Cliente.objects.all().filter(sexo='F')

