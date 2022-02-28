from django.db import models
from equipos.models import Equipo

# Create your models here.

class Jugador(models.Model):
  name = models.CharField(verbose_name="Nombre", max_length=16)
  last_name = models.CharField(verbose_name="Apellido", max_length=16)
  email = models.CharField(verbose_name="Email", max_length=64)
  alias = models.CharField(verbose_name="Alias", max_length=16)
  equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
  updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
  active = models.BooleanField(verbose_name="Activo")

  class Meta:
    verbose_name = "Jugador"
    verbose_name_plural = "Jugadores"
    ordering = ['-name']

  def __str__(self) -> str:
    return f"{self.name} {self.last_name}"
