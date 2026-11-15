"""Modelos persistentes y relación entre categorías y lugares."""
from django.db import models


class Categoria(models.Model):
    """Agrupa lugares históricos o turísticos bajo un tipo común."""

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre


class Lugar(models.Model):
    """Lugar patrimonial perteneciente obligatoriamente a una categoría."""

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="lugares",
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=200, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    """Actividad cultural asociada con un lugar patrimonial."""

    lugar = models.ForeignKey(
        Lugar,
        on_delete=models.PROTECT,
        related_name="eventos",
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["fecha", "nombre"]

    def __str__(self):
        return self.nombre
