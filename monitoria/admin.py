from django.contrib import admin

from .models import (
    Curso,
    Disciplina,
    Monitoria,
    Avaliacao,
)

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Monitoria)
admin.site.register(Avaliacao)