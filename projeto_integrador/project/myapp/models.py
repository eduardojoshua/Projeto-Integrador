from django.utils import timezone
from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    numero_matricula = models.IntegerField(unique=True, default=0)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    email = models.EmailField()
    data_matricula = models.CharField(max_length=10)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

