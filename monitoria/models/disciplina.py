from django.db import models
from monitoria.models import Curso

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    periodo = models.PositiveIntegerField()  # 1 a 10
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="disciplinas")

    def __str__(self):
        return self.nome
