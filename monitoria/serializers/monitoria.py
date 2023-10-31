from rest_framework.serializers import ModelSerializer
from monitoria.models import Monitoria

class MonitoriaSerializer(ModelSerializer):
    class Meta:
        model = Monitoria
        fields = "__all__"