from django.shortcuts import render 
from .models import Curso , Profesor, Estudiante
from django.http import HttpResponse

from .form import Profesorform


"""def crear_curso(request):
      

      nombre_curso = "Python"
      comision_curso = 51325

      curso = Curso(nombre = nombre_curso, comision = comision_curso)

      curso.save()

      respuesta = f"Curso creado --- {nombre_curso} --- {comision_curso}"

      return HttpResponse(respuesta)"""


def Cursos(request):
      return render(request , 'template/Cursos.html') 
 
def Estudiantes(request):

      estudiantes = Estudiante.objects.all()
      contex = {"estudiantes":estudiantes}

      return render (request ,'template/Estudiantes.html',contex) 

def Profesores(request):

      if request.method == "POST":
            
            form = Profesorform(request.POST)
            if form.is_valid():
                 
                  profesor = Profesor()
                  profesor.nombre = form.cleaned_data["nombre"]
                  profesor.apellido = form.cleaned_data["apellido"]
                  profesor.email = form.cleaned_data["email"]
                  profesor.profecion = form.cleaned_data["profecion"]

                  profesor.save()
                  form = Profesorform()
             
      else:
            form = Profesorform()


      profesores = Profesor.objects.all()
      context = {"profesores": profesores, "form":form}
      return render (request,'template/Profesores.html', context) 

def Entregables(request):
      return render (request, 'template/Entregables.html') 

def inicio(request):
      return render(request ,'template/inicio.html')

def InicioApp(request):
      return render(request ,'template/InicioApp.html')
