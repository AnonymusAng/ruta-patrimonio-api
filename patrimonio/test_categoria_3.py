from rest_framework.test import APITestCase

from patrimonio.models import Categoria


class CategoriaDeleteTests(APITestCase):
    def test_elimina_categoria_sin_lugares(self):
        category = Categoria.objects.create(nombre="Museos")
        response = self.client.delete(f"/api/categorias/{category.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Categoria.objects.filter(pk=category.pk).exists())
