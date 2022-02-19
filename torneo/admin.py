from django.contrib import admin
from .models import Temporada

# Register your models here.

class TemporadaAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')

admin.site.register(Temporada, TemporadaAdmin)