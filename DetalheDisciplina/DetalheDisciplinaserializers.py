from rest_framework import serializers
from DetalheDisciplina.models import DetalheDisciplina

class DetalheDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheDisciplina
        fields = [

            'codigoCurso',
            'codigoDisciplina',
        ]