"""Validación y conversión entre modelos Python y respuestas JSON."""
from rest_framework import serializers

from .models import Categoria, Evento, Lugar


class CategoriaSerializer(serializers.ModelSerializer):
    """Campos editables para crear, consultar y actualizar categorías."""

    class Meta:
        model = Categoria
        fields = ["id", "nombre", "descripcion"]


class LugarSerializer(serializers.ModelSerializer):
    """Expone la clave foránea y el nombre legible de la categoría."""

    categoria_nombre = serializers.CharField(source="categoria.nombre", read_only=True)

    class Meta:
        model = Lugar
        fields = [
            "id",
            "categoria",
            "categoria_nombre",
            "nombre",
            "descripcion",
            "direccion",
            "activo",
        ]


class EventoSerializer(serializers.ModelSerializer):
    """Devuelve el lugar asociado junto a su identificador."""

    lugar_nombre = serializers.CharField(source="lugar.nombre", read_only=True)

    class Meta:
        model = Evento
        fields = ["id", "lugar", "lugar_nombre", "nombre", "descripcion", "fecha", "activo"]
