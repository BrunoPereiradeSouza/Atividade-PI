from django.contrib import admin
from locadora.models import Cliente, Categoria, Filme, Locacao
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor', 'categoria')



@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data')
