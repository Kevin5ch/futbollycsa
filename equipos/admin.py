from django.contrib import admin
from .models import Equipo
# Register your models here.


class EquipoAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')
  search_fields = ('name','alias')
  #list_filter = ('name',)
  list_display = ('name','alias','active')
  date_hierarchy = 'created_at'

admin.site.register(Equipo, EquipoAdmin)
