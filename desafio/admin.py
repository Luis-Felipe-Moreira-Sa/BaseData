from django.contrib import admin
from .models import Cliente
# Register your models here.

admin.site.register(Cliente)
class Clientes(admin.ModelAdmin):
    list_display = ('id_codigo', 'nome', 'sobrenome', 'sexo', 'altura', 'peso', 'nascimento', 'bairro', 'cidade', 'estado', 'numero')
    list_display_links = ('id_codigo', 'nome')
    search_fields = ('nome',)
    list_per_page = 40
