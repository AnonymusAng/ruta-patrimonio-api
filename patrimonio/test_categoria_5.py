from rest_framework.test import APITestCase

from patrimonio.models import Categoria, Lugar


class CategoriaConstraintsTests(APITestCase):
    def test_nombre_unico_y_proteccion_de_categoria_con_lugares(self):
        category = Categoria.objects.create(nombre="Museos")
        duplicate = self.client.post("/api/categorias/", {"nombre": "Museos"}, format="json")
        self.assertEqual(duplicate.status_code, 400)
        Lugar.objects.create(categoria=category, nombre="Museo", descripcion="Colección local")
        deletion = self.client.delete(f"/api/categorias/{category.id}/")
        self.assertEqual(deletion.status_code, 400)
        self.assertTrue(Categoria.objects.filter(pk=category.pk).exists())
