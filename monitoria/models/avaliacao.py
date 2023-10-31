from django.db import models
from monitoria.models import Monitoria
from usuario.models import Usuario

class Avaliacao(models.Model):
    pontuacao = models.PositiveIntegerField()  # 0 a 5
    descricao = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monitoria = models.ForeignKey(Monitoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pontuação de {self.usuario.nome}: {self.pontuacao}"
    
    class Meta:
        verbose_name_plural = "Avaliacoes"