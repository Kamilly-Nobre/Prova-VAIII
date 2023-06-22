from rest_framework import viewsets
from .models import DetalheTurma
from DetalheTurma import DetalheTurmaserializers

class DetalheTurmaView (viewsets.ModelViewSet):
    queryset = DetalheTurma.objects.all()
    serializer_class = DetalheTurmaserializers

