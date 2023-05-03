
from django.urls import path
from PrimeraApp import views 
from django.contrib.auth.views import LogoutView




urlpatterns = [
   
    path('', views.InicioApp, name="inicioApp"),
    #path('crear_curso/', views.crear_curso ),
    path('cursos/' , views.Cursos, name="cursos"),
    path('profesores/' , views.Profesores, name="profesores"),
    path('estudiantes/' , views.Estudiantes,name="estudiantes"),
    path('entregables/', views.Entregables, name="entregables" ),
    path('buscar_comision/', views.buscar_comision, name="buscar_comision"),
    path('buscar/', views.buscar, name ="buscar"),
    path('eliminar_profesor/<id>', views.eliminar_profesor, name='eliminar_profesor'),
    path('editar_profesor/<id>', views.editar_profesor, name="editar_profesor"),
   
    path('registrar_usuario/', views.registrar_usuario, name= 'registrar_usuario'),
    path("login/", views.loguear_usuario, name = 'login'),
    path("logout/", LogoutView.as_view(template_name = "template/logout.html"), name = 'logout'), #esta es la vista que Deslogua el perfil cargado, en "template_name indicamos la ruta del temple que va a mostrarnos al estar deslogueado"
]
    