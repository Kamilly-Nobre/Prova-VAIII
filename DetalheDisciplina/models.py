from django.db import models

class DetalheDisciplina(models.Model):
    codigoCurso = models.CharField(max_length=100)
    codigoDisciplina = models.CharField(max_length=100)