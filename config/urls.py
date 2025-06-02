"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
path('admin/', admin.site.urls),
path('', IndexView.as_view(), name='index'),
  path('pessoa/', PessoaListView.as_view(), name='pessoa-list'),
    path('cidade/', CidadeListView.as_view(), name='cidade-list'),
    path('ocupacao/', OcupacaoListView.as_view(), name='ocupacao-list'),
    path('instituicaoensino/', InstituicaoListView.as_view(), name='instituicaoensino'),
    path('areasaber/', AreaSaberListView.as_view(), name='area-saber-list'),
    path('avaliacaotipo/', AvaliacaoTipoListView.as_view(), name='avaliacao-tipo-list'),
    path('curso/', CursoListView.as_view(), name='curso-list'),
   path('cursodisciplina/', CursoDisciplinaListView.as_view(), name='curso-disciplina-list'),
    path('turma/', TurmaListView.as_view(), name='turma-list'),
    path('disciplina/', DisciplinaListView.as_view(), name='disciplina-list'),
    path('disciplina/criar/', DisciplinaCreateView.as_view(), name='disciplina_create'),
    path('matricula/', MatriculaListView.as_view(), name='matricula-list'),
    path('frequencia/', FrequenciaListView.as_view(), name='frequencia-list'),
    path('avaliacao/', AvaliacaoListView.as_view(), name='avaliacao-list'),
    path('turno/', TurnoListView.as_view(), name='turno-list'),
    path('ocorrencia/', OcorrenciaListView.as_view(), name='ocorrencia-list'),
]
