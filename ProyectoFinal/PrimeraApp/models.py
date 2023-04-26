from django.db import models


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} - {self.apellitod} - {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profecion = models.CharField(max_length=30)

    
    def __str__(self):
        return f"{self.nombre} - {self.apellitod} - {self.email} - {self.profecion}"

class Entregables(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField(max_length=20)
    entregado = models.BooleanField()

    
    def __str__(self):
        return f"{self.nombre} - {self.fechaDeEntrega} - {self.entregado}"
    