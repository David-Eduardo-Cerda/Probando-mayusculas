
from django.urls import path
from PrimeraApp import views 



urlpatterns = [
   
    path('', views.InicioApp, name="inicioApp"),
    #path('crear_curso/', views.crear_curso ),
    path('cursos/' , views.Cursos, name="cursos"),
    path('profesores/' , views.Profesores, name="profesores"),
    path('estudiantes/' , views.Estudiantes,name="estudiantes"),
    path('entregables/', views.Entregables, name="entregables" ),
    path('buscar_comision/', views.buscar_comision, name="buscar_comision"),
    path('buscar_comision/', views.buscar, name =" buscar "),
    

]
    