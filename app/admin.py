from django.contrib import admin
from .models import *

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria_total', 'duracao_meses')
    search_fields = ('nome',)
    inlines = [CursoDisciplinaInline, AvaliacaoInline]

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'telefone')
    search_fields = ('nome',)
    inlines = [CursoInline]

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email')
    search_fields = ('nome', 'cpf', 'email')
    inlines = [MatriculaInline, FrequenciaInline, OcorrenciaInline]

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class AvaliacaoTipoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class TurnosAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    search_fields = ('nome', 'uf')

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Curso, CursoAdmin)
admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Turma)
admin.site.register(AvaliacaoTipo, AvaliacaoTipoAdmin)
admin.site.register(Turno, TurnosAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Ocupacao, OcupacaoAdmin)