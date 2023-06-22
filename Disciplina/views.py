from rest_framework import viewsets
from .models import Disciplina
from Disciplina import Disciplinaserializers


class DisciplinaView (viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = Disciplinaserializers

