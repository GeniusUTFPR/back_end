from rest_framework.viewsets import ModelViewSet

from monitoria.models import Avaliacao
from monitoria.serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
  queryset = Avaliacao.objects.all()
  serializer_class = AvaliacaoSerializer