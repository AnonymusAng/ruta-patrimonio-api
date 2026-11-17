
from rest_framework.test import APITestCase

from patrimonio.models import Categoria, Evento, Lugar


class EventoConstraintsTests(APITestCase):
    def test_lugar_es_obligatorio_y_debe_existir(self):
        missing = self.client.post("/api/eventos/", {"nombre": "Sin lugar", "descripcion": "Prueba"}, format="json")
        unknown = self.client.post("/api/eventos/", {"lugar": 9999, "nombre": "Sin vínculo", "descripcion": "Prueba"}, format="json")
        self.assertEqual(missing.status_code, 400)
        self.assertEqual(unknown.status_code, 400)
