from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema, extend_schema_view
from .serializers import DatosGeneralesSerializer
from .models import DatosGenerales


@extend_schema_view(
    list=extend_schema(description='Permite obtener una lista de elementos'),
    retrieve=extend_schema(description='Permite obtener una elemento'),
    create=extend_schema(description='Permite crear un elemento'),
    update=extend_schema(description='Permite actualizar un elemento'),
    destroy=extend_schema(description='Permite eliminar un elemento'),
)
class DatosGeneralesViewSet(viewsets.ModelViewSet):
    queryset = DatosGenerales.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DatosGeneralesSerializer
