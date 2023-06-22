from rest_framework import serializers
from DetalheTurma.models import DetalheTurma

class DetalheTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheTurma
        fields = [

            'codigoAluno',
            'codigoProfessor',
            'codigoTurma',
        ]