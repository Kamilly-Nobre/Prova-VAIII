from rest_framework import viewsets
from .models import Curso
from Curso import Cursoserializers


class CursoView (viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = Cursoserializers
