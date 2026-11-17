from rest_framework.test import APITestCase

from patrimonio.models import Categoria, Evento, Lugar


class LugarConstraintsTests(APITestCase):
    def test_categoria_es_obligatoria_y_no_elimina_lugar_con_eventos(self):
        invalid = self.client.post(
            "/api/lugares/",
            {"nombre": "Sin categoría", "descripcion": "Prueba"},
            format="json",
        )
        self.assertEqual(invalid.status_code, 400)

        category = Categoria.objects.create(nombre="Arquitectura")
        place = Lugar.objects.create(
            categoria=category,
            nombre="Torre",
            descripcion="Monumento",
        )
        Evento.objects.create(
            lugar=place,
            nombre="Recorrido",
            descripcion="Visita guiada",
        )

        deletion = self.client.delete(f"/api/lugares/{place.id}/")
        self.assertEqual(deletion.status_code, 400)
