from rest_framework.viewsets import ModelViewSet

from monitoria.models import Disciplina
from monitoria.serializers import (
    DisciplinaSerializer,
    DisciplinaDetailSerializer,
    DisciplinaListSerializer,
)

class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list":
            return DisciplinaListSerializer
        elif self.action == "retrieve":
            return DisciplinaDetailSerializer
        return DisciplinaSerializer
