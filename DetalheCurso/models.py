from django.db import models

class DetalheCurso(models.Model):
    codigo_curso = models.CharField(max_length=100)
    codigo_turma = models.CharField(max_length=100)
