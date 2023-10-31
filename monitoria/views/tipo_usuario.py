from rest_framework.viewsets import ModelViewSet

from monitoria.models import TipoUsuario
from monitoria.serializers import TipoUsuarioSerializer

class TipoUsuarioViewSet(ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer