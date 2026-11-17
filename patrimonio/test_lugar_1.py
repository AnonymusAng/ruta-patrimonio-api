from rest_framework.test import APITestCase

from patrimonio.models import Categoria


class LugarCreateListTests(APITestCase):
    def test_crea_y_lista_lugares(self):
        category = Categoria.objects.create(nombre="Arquitectura")
        created = self.client.post(
            "/api/lugares/",
            {
                "categoria": category.id,
                "nombre": "Torre",
                "descripcion": "Monumento",
            },
            format="json",
        )

        self.assertEqual(created.status_code, 201)

        listing = self.client.get("/api/lugares/")
        self.assertEqual(listing.status_code, 200)
        self.assertEqual(listing.data[0]["nombre"], "Torre")
