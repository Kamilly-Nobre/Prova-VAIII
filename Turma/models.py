from django.db import models
 
class Turma(models.Model):
    codigo = models.CharField(max_length=100)
    codigoCurso = models.CharField(max_length=100)
    
    