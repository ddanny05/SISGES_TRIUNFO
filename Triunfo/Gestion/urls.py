from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SociosViewSet, DetalleSociosViewSet, ReunionesViewSet, AsistenciasViewSet, IngresosViewSet, EgresosViewSet, UsuariosViewSet

# Crea un router y registra las vistas
router = DefaultRouter()
router.register(r'socios', SociosViewSet)
router.register(r'detalle-socios', DetalleSociosViewSet)
router.register(r'reuniones', ReunionesViewSet)
router.register(r'asistencias', AsistenciasViewSet)
router.register(r'ingresos', IngresosViewSet)
router.register(r'egresos', EgresosViewSet)
router.register(r'usuarios', UsuariosViewSet)

# Define las URLs de la API
urlpatterns = [
    path('', include(router.urls)),
]