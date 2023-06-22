from rest_framework import viewsets
from .models import Aluno
from aluno import alunoserializers


class AlunoView (viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = alunoserializers
