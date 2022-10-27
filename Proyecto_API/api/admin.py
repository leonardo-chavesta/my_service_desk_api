from django.contrib import admin
from .models import Perfil, Usuario, Productos, Clientes, TecnicoAsignado, PrioridadIncidencia

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(TecnicoAsignado)
admin.site.register(PrioridadIncidencia)