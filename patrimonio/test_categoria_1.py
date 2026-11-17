from rest_framework.test import APITestCase


class CategoriaCreateListTests(APITestCase):
    def test_crea_y_lista_categorias(self):
        created = self.client.post(
            "/api/categorias/",
            {
                "nombre": "Museos",
                "descripcion": "Espacios culturales"
            },
            format="json"
        )

        self.assertEqual(created.status_code, 201)

        listing = self.client.get("/api/categorias/")

        self.assertEqual(listing.status_code, 200)
        self.assertEqual(listing.data[0]["nombre"], "Museos")
