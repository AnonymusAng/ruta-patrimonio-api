from rest_framework.test import APITestCase

from patrimonio.models import Categoria


class CategoriaRepresentationTests(APITestCase):
    def test_respuesta_expone_id_nombre_y_descripcion(self):
        Categoria.objects.create(nombre="Museos", descripcion="Colecciones")
        result = self.client.get("/api/categorias/").data[0]
        self.assertEqual(result["nombre"], "Museos")
        self.assertEqual(result["descripcion"], "Colecciones")
        self.assertIn("id", result)
