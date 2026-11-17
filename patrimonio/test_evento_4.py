
from rest_framework.test import APITestCase

from patrimonio.models import Categoria, Evento, Lugar


class EventoRepresentationTests(APITestCase):
    def test_respuesta_incluye_lugar_y_nombre_legible(self):
        category = Categoria.objects.create(nombre="Cultura")
        place = Lugar.objects.create(categoria=category, nombre="Teatro", descripcion="Escenario")
        event = Evento.objects.create(lugar=place, nombre="Festival", descripcion="Música")
        result = self.client.get(f"/api/eventos/{event.id}/").data
        self.assertEqual(result["lugar"], place.id)
        self.assertEqual(result["lugar_nombre"], "Teatro")
