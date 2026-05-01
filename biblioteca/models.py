from django.db import models
from .validators import *


class Author(models.Model):
    nombre = models.CharField(max_length=100, validators=[blank_validator])
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="libros"
    )
    fecha_publicacion = models.DateField()
    resumen = models.TextField(validators=[min_length_validator(15)])

    def __str__(self):
        return f"{self.titulo} by {self.autor.nombre if self.autor else '...'}"


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="resenas")
    texto = models.TextField()
    calificacion = models.IntegerField(validators=[range_validator(min_value=1, max_value=5)])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"
