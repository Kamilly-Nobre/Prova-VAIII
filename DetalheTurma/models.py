from django.db import models

class DetalheTurma(models.Model):
    codigoAluno = models.CharField(max_length=100)
    codigoProfessor = models.CharField(max_length=100)
    codigoTurma = models.CharField(max_length=100)

    def __str__(self):
        return self.codigoAluno