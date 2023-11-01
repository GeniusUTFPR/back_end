from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from monitoria.models import Disciplina
from monitoria.serializers import (
    DisciplinaSerializer,
    DisciplinaDetailSerializer,
)

class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["curso__id"]
    search_fields = ["nome"]
    
    def get_serializer_class(self):
        if self.action == "list":
            return DisciplinaDetailSerializer
        elif self.action == "retrieve":
            return DisciplinaDetailSerializer
        return DisciplinaSerializer
