from rest_framework.test import APITestCase

from patrimonio.models import Categoria


class CategoriaDetailUpdateTests(APITestCase):
    def test_consulta_y_actualiza_categoria(self):
        category = Categoria.objects.create(nombre="Museos")
        detail = self.client.get(f"/api/categorias/{category.id}/")
        self.assertEqual(detail.status_code, 200)
        updated = self.client.patch(
            f"/api/categorias/{category.id}/",
            {"descripcion": "Patrimonio local"},
            format="json"
        )
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.data["descripcion"], "Patrimonio local")
