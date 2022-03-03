from django.contrib import admin
from .models import Jugador
# Register your models here.


class JugadorAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')
  search_fields = ('name','last_name','equipo__name')
  list_filter = ('equipo',)
  list_display = ('nombres','alias','equipo')
  date_hierarchy = 'created_at'

  def nombres(self, obj):
    return f"{obj.name} {obj.last_name}"

admin.site.register(Jugador, JugadorAdmin)
