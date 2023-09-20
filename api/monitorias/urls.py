from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

from monitorias.views import CursoViewSet, UsuarioViewSet, DisciplinaViewSet, MonitoriaViewSet, AvaliacaoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'curso', CursoViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'disciplina', DisciplinaViewSet)
router.register(r'monitoria', MonitoriaViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)

urlpatterns = [
  path('', views.index, name='index'),
]