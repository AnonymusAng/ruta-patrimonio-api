"""Rutas REST generadas para los dos recursos de la práctica."""
from rest_framework.routers import DefaultRouter

from .views import CategoriaViewSet, EventoViewSet, LugarViewSet

router = DefaultRouter()
router.register("categorias", CategoriaViewSet, basename="categoria")
router.register("lugares", LugarViewSet, basename="lugar")
router.register("eventos", EventoViewSet, basename="evento")

urlpatterns = router.urls
