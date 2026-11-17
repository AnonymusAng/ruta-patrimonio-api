from rest_framework.test import APITestCase

from patrimonio.models import Categoria, Lugar


class LugarDetailUpdateTests(APITestCase):
    def test_consulta_y_actualiza_lugar(self):
        category = Categoria.objects.create(nombre="Arquitectura")
        place = Lugar.objects.create(
            categoria=category,
            nombre="Torre",
            descripcion="Monumento",
        )

        response = self.client.get(f"/api/lugares/{place.id}/")
        self.assertEqual(response.status_code, 200)

        updated = self.client.patch(
            f"/api/lugares/{place.id}/",
            {"direccion": "Parque Caldas"},
            format="json",
        )
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.data["direccion"], "Parque Caldas")
