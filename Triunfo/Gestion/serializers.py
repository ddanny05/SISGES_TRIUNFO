from rest_framework import serializers
from .models import Socios, Detalle_Socios, Reuniones, Asistencias, Ingresos, Egresos, Usuarios

# Serializer para el modelo Socios
class SociosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socios
        fields = '__all__'  # Incluye todos los campos del modelo

# Serializer para el modelo Detalle_Socios
class DetalleSociosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Socios
        fields = '__all__'

# Serializer para el modelo Reuniones
class ReunionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reuniones
        fields = '__all__'

# Serializer para el modelo Asistencias
class AsistenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencias
        fields = '__all__'

# Serializer para el modelo Ingresos
class IngresosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresos
        fields = '__all__'

# Serializer para el modelo Egresos
class EgresosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egresos
        fields = '__all__'

# Serializer para el modelo Usuarios
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'