from rest_framework.test import APITestCase

from patrimonio.models import Categoria, Lugar


class LugarDeleteTests(APITestCase):
    def test_elimina_lugar_sin_eventos(self):
        category = Categoria.objects.create(nombre="Arquitectura")
        place = Lugar.objects.create(
            categoria=category,
            nombre="Torre",
            descripcion="Monumento",
        )

        response = self.client.delete(f"/api/lugares/{place.id}/")

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Lugar.objects.filter(pk=place.pk).exists())
