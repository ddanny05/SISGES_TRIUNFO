from django.shortcuts import render
from rest_framework import viewsets
from .models import Socios, Detalle_Socios, Reuniones, Asistencias, Ingresos, Egresos, Usuarios
from .serializers import SociosSerializer, DetalleSociosSerializer, ReunionesSerializer, AsistenciasSerializer, IngresosSerializer, EgresosSerializer, UsuariosSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated #para que se accedan solo los usuarios con permisos

# Vista para el modelo Socios
class SociosViewSet(viewsets.ModelViewSet):
    queryset = Socios.objects.all()
    serializer_class = SociosSerializer
    permission_classes = [AllowAny] #todos pueden acceder a esta vista / API


# Vista para el modelo Detalle_Socios
class DetalleSociosViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Socios.objects.all()
    serializer_class = DetalleSociosSerializer
    permission_classes = [AllowAny] #todos pueden accerder a esta vista / API

# Vista para el modelo Reuniones
class ReunionesViewSet(viewsets.ModelViewSet):
    queryset = Reuniones.objects.all()
    serializer_class = ReunionesSerializer
    permission_classes = [AllowAny]

# Vista para el modelo Asistencias
class AsistenciasViewSet(viewsets.ModelViewSet):
    queryset = Asistencias.objects.all()
    serializer_class = AsistenciasSerializer
    permission_classes = [AllowAny]

# Vista para el modelo Ingresos
class IngresosViewSet(viewsets.ModelViewSet):
    queryset = Ingresos.objects.all()
    serializer_class = IngresosSerializer
    permission_classes = [AllowAny]

# Vista para el modelo Egresos
class EgresosViewSet(viewsets.ModelViewSet):
    queryset = Egresos.objects.all()
    serializer_class = EgresosSerializer
    permission_classes = [AllowAny]

# Vista para el modelo Usuarios
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [AllowAny]