from rest_framework.serializers import ModelSerializer
from monitoria.models import TipoUsuario

class TipoUsuarioSerializer(ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = "__all__"