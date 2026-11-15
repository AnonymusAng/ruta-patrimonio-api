"""Permite inspeccionar y administrar datos desde Django Admin."""
from django.contrib import admin

from .models import Categoria, Evento, Lugar


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]
    search_fields = ["nombre"]


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "categoria", "activo"]
    list_filter = ["categoria", "activo"]
    search_fields = ["nombre", "descripcion", "direccion"]


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "lugar", "fecha", "activo"]
    list_filter = ["fecha", "activo"]
    search_fields = ["nombre", "descripcion", "lugar__nombre"]
