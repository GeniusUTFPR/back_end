from django.db import models
from django.contrib.auth.hashers import make_password

class Curso(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    tipo = models.PositiveIntegerField()  # Estudante, Monitor pago, Monitor, Professor, Administrador
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    registro = models.CharField(max_length=255)  # Registro acadêmico
    celular = models.CharField(max_length=20, null=True, blank=True)
    foto_perfil = models.URLField(max_length=255, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Verifique se é uma criação de objeto e não uma atualização
            self.senha = make_password(self.senha)
        super(Usuario, self).save(*args, **kwargs)

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    periodo = models.PositiveIntegerField()  # 1 a 10
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Monitoria(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.PositiveIntegerField()
    valor_por_hora = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"Monitoria de {self.disciplina.nome} por usuário {self.usuario.nome}"

class Avaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    pontuacao = models.PositiveIntegerField()  # 0 a 5
    descricao = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monitoria = models.ForeignKey(Monitoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pontuação de {self.usuario.nome}: {self.pontuacao}"
