from rest_framework.serializers import ModelSerializer
from monitoria.models import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = "__all__"