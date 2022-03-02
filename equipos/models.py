from django.db import models

# Create your models here.

class Equipo(models.Model):
  name = models.CharField(verbose_name="Nombre", max_length=16)
  alias = models.CharField(verbose_name="Alias", max_length=16)
  logo = models.ImageField(default='null', upload_to="equipos")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
  active = models.BooleanField(verbose_name="Activo", default=True)

  class Meta:
    verbose_name = "Equipo"
    verbose_name_plural = "Equipos"
    ordering = ['-name']


  def __str__(self) -> str:
    return f"{self.name} ({self.alias})"
