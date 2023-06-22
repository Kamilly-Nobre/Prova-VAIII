from rest_framework import serializers
from Curso.models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = [

            'codigo',
            'nome',
        ]