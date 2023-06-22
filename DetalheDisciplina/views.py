from rest_framework import viewsets
from .models import DetalheDisciplina
from DetalheDisciplina import DetalheDisciplinaserializers

class DetalheDisciplinaView (viewsets.ModelViewSet):
    queryset = DetalheDisciplina.objects.all()
    serializer_class = DetalheDisciplinaserializers

