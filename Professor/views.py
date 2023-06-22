from rest_framework import viewsets
from .models import Professor
from Professor import Professorserializers


class ProfessorView (viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = Professorserializers

