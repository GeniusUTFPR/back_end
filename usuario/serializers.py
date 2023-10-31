from rest_framework.serializers import ModelSerializer

from .models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class UsuarioDetailSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        depth = 1