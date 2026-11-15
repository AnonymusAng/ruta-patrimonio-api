"""ViewSets que ofrecen las operaciones CRUD de la API."""
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Categoria, Evento, Lugar
from .serializers import CategoriaSerializer, EventoSerializer, LugarSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    """CRUD de categorías; protege las categorías que aún tienen lugares."""

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def destroy(self, request, *args, **kwargs):
        categoria = self.get_object()
        if categoria.lugares.exists():
            return Response(
                {"detail": "No se puede eliminar una categoría que tiene lugares asociados."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().destroy(request, *args, **kwargs)


class LugarViewSet(viewsets.ModelViewSet):
    """CRUD de lugares; carga la categoría en la misma consulta."""

    queryset = Lugar.objects.select_related("categoria").all()
    serializer_class = LugarSerializer

    def destroy(self, request, *args, **kwargs):
        lugar = self.get_object()
        if lugar.eventos.exists():
            return Response(
                {"detail": "No se puede eliminar un lugar que tiene eventos asociados."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().destroy(request, *args, **kwargs)


class EventoViewSet(viewsets.ModelViewSet):
    """CRUD de eventos culturales asociados a un lugar."""

    queryset = Evento.objects.select_related("lugar").all()
    serializer_class = EventoSerializer
