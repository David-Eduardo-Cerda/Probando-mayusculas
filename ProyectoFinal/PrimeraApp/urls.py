
from django.urls import path
from PrimeraApp import views 



urlpatterns = [
   
    path('', views.InicioApp, name="inicioApp"),
    #path('crear_curso/', views.crear_curso ),
    path('Cursos/' , views.Cursos, name="cursos"),
    path('Profesores/' , views.Profesores, name="profesores"),
    path('Estudiantes/' , views.Estudiantes,name="estudiantes"),
    path('Entregables/', views.Entregables, name="entregables" ),

]
    