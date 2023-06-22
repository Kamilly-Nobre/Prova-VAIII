from rest_framework import serializers
from Disciplina.models import Disciplina

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = [

            'codigo',
            'nome',
        ]