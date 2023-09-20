from django.shortcuts import render
from rest_framework import viewsets
from .models import Curso, Usuario, Disciplina, Monitoria, Avaliacao 
from .serializers import CursoSerializer, UsuarioSerializer, DisciplinaSerializer, MonitoriaSerializer, AvaliacaoSerializer 
from django.http import HttpResponse

def index(request):
  return HttpResponse('Teste')

class CursoViewSet(viewsets.ModelViewSet):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
  queryset = Disciplina.objects.all()
  serializer_class = DisciplinaSerializer

class MonitoriaViewSet(viewsets.ModelViewSet):
  queryset = Monitoria.objects.all()
  serializer_class = MonitoriaSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
  queryset = Avaliacao.objects.all()
  serializer_class = AvaliacaoSerializer


