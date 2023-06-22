from rest_framework import serializers
from Professor.models import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = [

            'nome',
            'sexo',
            'registro',
        ]