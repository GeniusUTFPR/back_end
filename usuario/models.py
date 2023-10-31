from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from monitoria.models import Curso, TipoUsuario

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(_("E-mail"), unique=True)
    nome = models.CharField(_("Nome completo"), max_length=255, blank=True, null=False)
    celular = models.CharField(_("Celular"), max_length=11, blank=True, null=True)
    registro = models.CharField(_("Registro acadêmico"), max_length=255, blank=True, null=False)  # Registro acadêmico
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, default=1, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=1, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-date_joined"]
