from django.db import models
from monitoria.models import Disciplina
from usuario.models import Usuario

class Monitoria(models.Model):
    tipo_monitoria = models.PositiveIntegerField()
    valor_por_hora = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    horarios = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"Monitoria de {self.disciplina.nome} do usuário {self.usuario.nome}"