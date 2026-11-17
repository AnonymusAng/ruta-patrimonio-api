from rest_framework.test import APITestCase

from patrimonio.models import Categoria, Lugar


class LugarRepresentationTests(APITestCase):
    def test_respuesta_incluye_categoria_y_nombre_legible(self):
        category = Categoria.objects.create(nombre="Arquitectura")
        place = Lugar.objects.create(
            categoria=category,
            nombre="Torre",
            descripcion="Monumento",
        )

        result = self.client.get(f"/api/lugares/{place.id}/").data

        self.assertEqual(result["categoria"], category.id)
        self.assertEqual(result["categoria_nombre"], "Arquitectura")
