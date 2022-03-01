from tabnanny import verbose
from django.db import models
from equipos.models import Equipo
from torneo.models import Cancha
#Create your models here. 

class Partido(models.Model):
  date = models.DateField(verbose_name="Dia")
  time = models.TimeField(verbose_name="Hora")
  local = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, verbose_name="Local")
  #visit = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, verbose_name="Visitante")
  stadium = models.ForeignKey(Cancha, on_delete=models.SET_NULL, null=True, verbose_name="Cancha")
  STATUS_MATCH = [
    ('PD', 'Pendiente'),
    ('SP', 'Suspendido'),
    ('TR', 'Terminado')
  ]
  status = models.CharField(max_length=2, choices=STATUS_MATCH, verbose_name="Estado del partido")
  alias = models.CharField(verbose_name="Alias",max_length=16)
  updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
  active = models.BooleanField(verbose_name="Activo")

  class Meta:
    verbose_name = "Partido"
    verbose_name_plural = "Partidos"
    ordering = ['-date']

  def __str__(self) -> str:
    return f"{self.name} {self.last_name}"
