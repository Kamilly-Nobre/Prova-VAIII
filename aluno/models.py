from django.db import models

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    data_Dascimento = models.CharField(max_length=100)
    
