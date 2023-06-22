"""
URL configuration for Prova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from aluno.views import AlunoView
from Curso.views import CursoView
from DetalheCurso.views import DetalheCursosView
from DetalheDisciplina.views import DetalheDisciplinaView
from DetalheTurma.views import DetalheTurmaView
from Disciplina.views import DisciplinaView
from Professor.views import ProfessorView
from Turma.views import TurmaView

rotas = routers.DefaultRouter()
rotas.register(r'aluno',AlunoView, basename='Aluno'),
rotas.register(r'Curso',CursoView, basename='Curso'),
rotas.register(r'DetalheCurso',DetalheCursosView, basename='DetalheCurso'),
rotas.register(r'DetalheDisciplina',DetalheDisciplinaView, basename='DetalheDisciplina'),
rotas.register(r'DetalheTurma',DetalheTurmaView, basename='DetalheTurma'),
rotas.register(r'Disciplina',DisciplinaView, basename='Disciplina'),
rotas.register(r'Professor',ProfessorView, basename='Professor'),
rotas.register(r'Turma',TurmaView, basename='Turma'),



urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api/', include(rotas.urls)),
]
