
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

# Register your models here.
class CitaAdmin(admin.ModelAdmin):
    model = Cita
    list_display = ('fecha_cita', 'hora_cita', 'observacion', 'created') 

admin.site.register(Cita, CitaAdmin)
