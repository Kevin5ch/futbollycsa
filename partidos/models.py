from tabnanny import verbose
from django.db import models
from django.core.exceptions import ValidationError
from equipos.models import Equipo
from torneo.models import Cancha, Temporada
from jugadores.models import Jugador
#Create your models here. 

class Partido(models.Model):
  date = models.DateField(verbose_name="Dia")
  time = models.TimeField(verbose_name="Hora")
  local = models.ForeignKey(Equipo, on_delete=models.SET_NULL, related_name="local_team", null=True, verbose_name="Local")
  visit = models.ForeignKey(Equipo, on_delete=models.SET_NULL, related_name="visit_team", null=True, verbose_name="Visitante")
  stadium = models.ForeignKey(Cancha, on_delete=models.SET_NULL, null=True, verbose_name="Cancha")
  season = models.ForeignKey(Temporada, on_delete=models.SET_NULL, null=True, verbose_name="Temporada")
  STATUS_MATCH = [
    ('PD', 'Pendiente'),
    ('SP', 'Suspendido'),
    ('TR', 'Terminado')
  ]
  status = models.CharField(max_length=2, choices=STATUS_MATCH, verbose_name="Estado del partido")
  alias = models.CharField(verbose_name="Alias",max_length=16)
  updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
  active = models.BooleanField(verbose_name="Activo", default=True)

  class Meta:
    verbose_name = "Partido"
    verbose_name_plural = "Partidos"
    ordering = ['-date']

  def __str__(self) -> str:
    return f"{self.local} vs {self.visit}  ({(self.date).strftime('%d/%m/%Y')})"

  def clean(self):
    if self.local.id == self.visit.id:
      #print(f"Local -> {self.local.id}, visitante -> {self.visit.id}")
      raise ValidationError("Los equipos del partido deben ser diferentes")

class Gol(models.Model):
  player = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, verbose_name="Jugador")
  match = models.ForeignKey(Partido, on_delete=models.SET_NULL, null=True, verbose_name="Partido")
  goal_against = models.BooleanField(verbose_name="En contra")
  quantity = models.IntegerField(default=1, verbose_name="Gol / es")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
  active = models.BooleanField(verbose_name="Activo", default=True)

  class Meta:
    verbose_name = "Gol"
    verbose_name_plural = "Goles"
    #ordering = ['-id']

  def __str__(self) -> str:
    return f"{self.player}"