from django.contrib import admin
from django.urls import include, path
from monitorias.views import CursoViewSet, UsuarioViewSet, DisciplinaViewSet, MonitoriaViewSet, AvaliacaoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'curso', CursoViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'disciplina', DisciplinaViewSet)
router.register(r'monitoria', MonitoriaViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]