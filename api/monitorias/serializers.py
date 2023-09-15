from rest_framework import serializers
from .models import Curso, Usuario, Disciplina, Monitoria, Avaliacao


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome']

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = ['tipo', 'nome', 'email', 'senha', 'registro', 'celular', 'foto_perfil', 'curso']

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'periodo', 'curso']

class MonitoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoria
        fields = ['id', 'tipo', 'valor_por_hora', 'descricao', 'usuario', 'disciplina']

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'pontuacao', 'descricao', 'usuario', 'monitoria']