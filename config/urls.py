from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from monitoria.views import (
    CursoViewSet,
    DisciplinaViewSet,
    MonitoriaViewSet,
    AvaliacaoViewSet,
    TipoUsuarioViewSet,
)

from usuario.views import UsuarioViewSet

from usuario.router import router as usuario_router

router = DefaultRouter()
router.register(r"cursos", CursoViewSet)
router.register(r"disciplinas", DisciplinaViewSet)
router.register(r"usuarios", UsuarioViewSet)
router.register(r"monitorias", MonitoriaViewSet)
router.register(r"avaliacoes", AvaliacaoViewSet)
router.register(r"tipo_usuario", TipoUsuarioViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/", include(usuario_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]