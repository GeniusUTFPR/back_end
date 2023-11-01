from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from monitoria.models import Monitoria
from monitoria.serializers import (
  MonitoriaSerializer,
  MonitoriaDetailSerializer,
)

class MonitoriaViewSet(ModelViewSet):
  queryset = Monitoria.objects.all()
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ["id", "tipo_monitoria", "usuario__id", "disciplina__id"]
    
  def get_serializer_class(self):
      if self.action == "list":
          return MonitoriaDetailSerializer
      elif self.action == "retrieve":
          return MonitoriaDetailSerializer
      return MonitoriaSerializer
