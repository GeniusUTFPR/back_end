from rest_framework.viewsets import ModelViewSet
from monitoria.models import Monitoria
from monitoria.serializers import MonitoriaSerializer

class MonitoriaViewSet(ModelViewSet):
  queryset = Monitoria.objects.all()
  serializer_class = MonitoriaSerializer