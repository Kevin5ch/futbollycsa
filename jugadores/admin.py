from django.contrib import admin
from .models import Jugador
# Register your models here.


class JugadorAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at')


admin.site.register(Jugador, JugadorAdmin)
