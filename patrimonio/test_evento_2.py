
from rest_framework.test import APITestCase

from patrimonio.models import Categoria, Evento, Lugar


class EventoDetailUpdateTests(APITestCase):
    def test_consulta_y_actualiza_evento(self):
        category = Categoria.objects.create(nombre="Cultura")
        place = Lugar.objects.create(categoria=category, nombre="Teatro", descripcion="Escenario")
        event = Evento.objects.create(lugar=place, nombre="Festival", descripcion="Música")
        self.assertEqual(self.client.get(f"/api/eventos/{event.id}/").status_code, 200)
        updated = self.client.patch(f"/api/eventos/{event.id}/", {"nombre": "Festival local"}, format="json")
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.data["nombre"], "Festival local")
