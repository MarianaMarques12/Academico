from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from django.views.generic import ListView
from .models import Pessoa
from django.views.generic.edit import CreateView
from .models import Disciplina
from django.urls import reverse_lazy

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass
class PessoaListView(ListView):
    model = Pessoa
    template_name = 'pessoa.html'  # Nome do seu template
    context_object_name = 'pessoas'

class CidadeListView(ListView):
    model = Cidade
    template_name = 'cidade.html'
    context_object_name = 'cidades'

class OcupacaoListView(ListView):
    model = Ocupacao
    template_name = 'ocupacao.html'
    context_object_name = 'ocupacoes'
class InstituicaoListView(ListView):
    model = InstituicaoEnsino
    template_name = 'instituicaoensino.html'
    context_object_name = 'instituicoes'
class AreaSaberListView(ListView):
    model = AreaSaber
    template_name = 'areasaber.html'
    context_object_name = 'areas'
class AvaliacaoTipoListView(ListView):
    model = AvaliacaoTipo
    template_name = 'avaliacaotipo.html'
    context_object_name = 'tipos'

class CursoListView(ListView):
    model = Curso
    template_name = 'curso.html'
    context_object_name = 'cursos'
    
class DisciplinaCreateView(CreateView):
    model = Disciplina
    fields = ['nome', 'outro_campo']  # substitua pelos campos do seu model
    template_name = 'disciplina_form.html'  # crie esse template
    success_url = reverse_lazy('disciplina-list')

class TurmaListView(ListView):
    model = Turma
    template_name = 'turma.html'
    context_object_name = 'turmas'


class DisciplinaListView(ListView):
    model = Disciplina
    template_name = 'disciplina.html'
    context_object_name = 'disciplinas'

class MatriculaListView(ListView):
    model = Matricula
    template_name = 'matricula.html'
    context_object_name = 'matriculas'

class FrequenciaListView(ListView):
    model = Frequencia
    template_name = 'frequencia.html'
    context_object_name = 'frequencias'

class AvaliacaoListView(ListView):
    model = Avaliacao
    template_name = 'avaliacao.html'
    context_object_name = 'avaliacoes'


class TurnoListView(ListView):
    model = Turno
    template_name = 'turno.html'
    context_object_name = 'turnos'

class OcorrenciaListView(ListView):
    model = Ocorrencia
    template_name = 'ocorrencia.html'
    context_object_name = 'ocorrencias'


class CursoDisciplinaListView(ListView):
    model = CursoDisciplina
    template_name = 'cursodisciplina.html'
    context_object_name = 'cursodisciplinas'


