from django.contrib import admin
from .models import  Noticia, Evento, Proyecto, Carrera, Periodo

# Register your models here.
admin.site.register(Periodo)
admin.site.register(Noticia)
admin.site.register(Evento)
admin.site.register(Proyecto)
admin.site.register(Carrera)