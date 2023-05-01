from django.shortcuts import render 
from .models import Curso , Profesor, Estudiante
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login , authenticate , logout

from .form import Profesorform , Estudiantesform


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

      if request.method == "POST":
            form = Estudiantesform(request.POST)
            if form.is_valid():
                  estudiante = Estudiante()
                  #cleaned_data = form.cleaned_data
                  estudiante.nombre = form.cleaned_data["nombre"]
                  estudiante.apellido = form.cleaned_data["apellido"]
                  estudiante.email = form.cleaned_data["email"]
                  estudiante.save()
                  form = Estudiantesform()
      else:
            form = Estudiantesform()           

      estudiantes = Estudiante.objects.all()
      contex = {"estudiantes":estudiantes, "form": form}

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


def buscar(request):

      comision = request.GET["comision"]
      if comision!='':
            cursos = Curso.objects.filter(comision__icontains = comision)
            return render(request, "template/resultados_busquedas.html", {"cursos": cursos})
      else:
            return render(request, "template/buscar_comision.html", {'mensaje':"Che ingresa una comision"})


def buscar_comision(request):
      return render(request, 'template/buscar_comision.html')

def eliminar_profesor(request, id):
      profesor = Profesor.objects.get(id=id)
      print(profesor)
      profesor.delete()
      profesores = Profesor.objects.all()
      form = Profesorform()
      return render(request , "template/profesores.html",{"profesores" : profesores, "mensaje": "Profesor eliminado", "form": form } )

def editar_profesor(request, id):
      profesor = Profesor.objects.get(id=id)
      if request.method=="POST":
            form = Profesorform(request.POST)
            if form.is_valid():
                  info = form.cleaned_data
                  profesor.nombre = info["nombre"]
                  profesor.apellido = info["apellido"]
                  profesor.email = info["email"]
                  profesor.profecion = info["profecion"]
                  profesor.save()
                  profesores = Profesor.objects.all()
                  return render(request, "template/profesores.html", {"profesores" : profesores, "mensaje" : "Profesore editado correctamente", "form" : form})
            pass
      else:
            formulario = Profesorform(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profecion})
            return render(request, "template/editar_profesor.html", {"form": formulario, "profesor":profesor})
      

def loguear_usuario(request):
      if request.method=="POST":
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                  info = form.cleaned_data
                  usu = info["username"]
                  clave = info['password']
                  usuario = authenticate(username = usu , password = clave)
                  if usuario is not None:
                        login(request,usuario)
                        return render(request , "template/inicio.html", {"mensaje" : f"Usuario {usu} logueado correctamente"})
                  else:
                        return render(request, "template/login.html", {'form': form , "mensaje":"Usuario o contrasenia incorrectos"})
            else:
                  return render(request , "template/login.html" , {"form": form, "mensaje" : "Usuario o contrasenia incorrectos"})
      else:
            form = AuthenticationForm()
            return render( request, "template/login.html", {"form": form})
      

def registrar_usuario(request):
      if request.method=="POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data.get("username")
                  form.save()
                  return render(request , "template/inicio.html", {"mensaje" : f"Usuario {username} registrado correctamente"})
                  
            else:
                  return render(request , "template/registrar_usuario.html" , {"form": form, "mensaje" : "Error al crear usuario"})
      else:
            form = UserCreationForm()
            return render( request, "template/registrar_usuario.html", {"form": form})


                        