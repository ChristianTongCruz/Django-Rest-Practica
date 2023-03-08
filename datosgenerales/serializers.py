from rest_framework import serializers
from .models import DatosGenerales


class DatosGeneralesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosGenerales
        fields = ('id_datos_generales', 'lugar_nacimiento', 'sexo', 'edad',
                  'estado_civil', 'residencia_permanente_vivienda', 'numero_piso_vivienda')
        read_only_fields = ('id_datos_generales', )
