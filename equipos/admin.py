from django.contrib import admin
from .models import Equipo
# Register your models here.


class EquipoAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')


admin.site.register(Equipo, EquipoAdmin)
