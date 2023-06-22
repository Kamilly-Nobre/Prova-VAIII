from rest_framework import serializers
from aluno.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
        
        'nome',
        'sexo',
        'matricula',
        'data_Nascimento',

        ]