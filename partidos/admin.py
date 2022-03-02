from django.contrib import admin
from .models import Partido, Gol
# Register your models here.

class PartidoAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')

admin.site.register(Partido, PartidoAdmin)

class GolAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')

admin.site.register(Gol, GolAdmin)