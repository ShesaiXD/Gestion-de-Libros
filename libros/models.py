from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField(
        validators=[
            MinValueValidator(1),  # El año no puede ser 0 ni negativo
            MaxValueValidator(datetime.datetime.now().year)  # No puede ser mayor al año actual
        ]
    )
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
