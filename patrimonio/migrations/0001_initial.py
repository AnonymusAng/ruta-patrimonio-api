"""Migración inicial para categorías y lugares patrimoniales."""
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=100, unique=True)),
                ("descripcion", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "categoría",
                "verbose_name_plural": "categorías",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Lugar",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=150)),
                ("descripcion", models.TextField()),
                ("direccion", models.CharField(blank=True, max_length=200)),
                ("activo", models.BooleanField(default=True)),
                ("categoria", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="lugares", to="patrimonio.categoria")),
            ],
            options={"ordering": ["nombre"]},
        ),
        migrations.CreateModel(
            name="Evento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=150)),
                ("descripcion", models.TextField()),
                ("fecha", models.DateField(blank=True, null=True)),
                ("activo", models.BooleanField(default=True)),
                ("lugar", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="eventos", to="patrimonio.lugar")),
            ],
            options={"ordering": ["fecha", "nombre"]},
        ),
    ]
