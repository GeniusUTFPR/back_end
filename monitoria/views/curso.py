from rest_framework.viewsets import ModelViewSet

from monitoria.models import Curso
from monitoria.serializers import CursoSerializer

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer