from django.contrib import admin
from .models import Temporada, Cancha

# Register your models here.

class TemporadaAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')
  search_fields = ('name','start_dayf')
  list_filter = ('active',)
  list_display = ('name','start_dayf','active')
  date_hierarchy = 'start_day'

  def start_dayf(self, obj):
    return f"{(obj.start_day).strftime('%d/%m/%Y')}"
    
admin.site.register(Temporada, TemporadaAdmin)

class CanchaAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')
  search_fields = ('name',)
  list_filter = ('active',)
  list_display = ('name','active')
  date_hierarchy = 'created_at'

admin.site.register(Cancha, CanchaAdmin)