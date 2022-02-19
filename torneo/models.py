from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.
class Temporada(models.Model):
  name = models.CharField(verbose_name="Nombre de temporada", max_length=128)
  description = models.TextField(verbose_name="Descripcion")
  start_day = models.DateField(verbose_name="Fecha de inicio")
  logo = models.ImageField(default='null', upload_to="temporadas")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
  active = models.BooleanField(verbose_name="Activo")

  class Meta:
    verbose_name = "Temporada"
    verbose_name_plural = "Temporadas"
    ordering = ['-id']

  def __str__(self) -> str:
      return f"{self.name}"