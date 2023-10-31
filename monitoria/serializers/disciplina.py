from rest_framework.serializers import ModelSerializer
from monitoria.models import Disciplina

class DisciplinaSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = "__all__"

class DisciplinaDetailSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = "__all__"
        depth = 1

class DisciplinaListSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ["nome", "periodo"]