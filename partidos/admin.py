from django.contrib import admin
from .models import Partido, Gol
# Register your models here.

class PartidoAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')
  search_fields = ('local__name','visit__name','stadium__name')
  list_filter = ('date','time','status')
  list_display = ('equipos','dia','time','stadium','season')
  date_hierarchy = 'date'


  def equipos(self, obj):
    return f"{obj.local} vs {obj.visit}"

  def dia(self, obj):
    return f"{(obj.date).strftime('%d/%m/%Y')}"


admin.site.register(Partido, PartidoAdmin)

class GolAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')
  search_fields = ('player__name','player__last_name')
  list_filter = ('player','match','goal_against')
  list_display = ('player','match','quantity','goal_against')
  date_hierarchy = 'created_at'

admin.site.register(Gol, GolAdmin)