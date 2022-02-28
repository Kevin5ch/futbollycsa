from django.contrib import admin
from .models import Temporada, Cancha

# Register your models here.

class TemporadaAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')

admin.site.register(Temporada, TemporadaAdmin)

class CanchaAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')

admin.site.register(Cancha, CanchaAdmin)