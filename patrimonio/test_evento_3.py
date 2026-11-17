
from rest_framework.test import APITestCase

from patrimonio.models import Categoria, Evento, Lugar


class EventoDeleteTests(APITestCase):
    def test_elimina_evento(self):
        category = Categoria.objects.create(nombre="Cultura")
        place = Lugar.objects.create(categoria=category, nombre="Teatro", descripcion="Escenario")
        event = Evento.objects.create(lugar=place, nombre="Festival", descripcion="Música")
        response = self.client.delete(f"/api/eventos/{event.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Evento.objects.filter(pk=event.pk).exists())
