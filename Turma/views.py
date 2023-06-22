from rest_framework import viewsets
from .models import Turma
from Turma import Turmaserializers

class TurmaView (viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = Turmaserializers

