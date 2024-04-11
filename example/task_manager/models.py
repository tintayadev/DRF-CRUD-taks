from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField(null=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre