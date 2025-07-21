from django.db import models
from usuarios.models import Usuario
# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas', null=True, blank=True)

    def __str__(self):
        return self.titulo