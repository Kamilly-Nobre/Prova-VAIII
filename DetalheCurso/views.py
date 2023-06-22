from rest_framework import viewsets
from .models import DetalheCurso
from DetalheCurso import DetalheCursoserializers

class DetalheCursosView (viewsets.ModelViewSet):
    queryset = DetalheCurso.objects.all()
    serializer_class = DetalheCursoserializers
