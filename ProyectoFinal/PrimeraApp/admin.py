from django.contrib import admin
from .models import Curso , Profesor , Entregables , Estudiante

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Entregables)
admin.site.register(Estudiante)
