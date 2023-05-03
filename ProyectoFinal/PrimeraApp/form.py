from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Profesorform(forms.Form):
    nombre = forms.CharField(max_length=30, label="Nombre del profesor")
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profecion = forms.CharField(max_length=30)


class Estudiantesform(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class Registro_usuario_form(UserCreationForm):
    email = forms.EmailField(label="Email usuario")
    password1 = forms.CharField(label="Contrasenia", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contrasenia", widget= forms.PasswordInput)

    class Meta:
        model=User
        fields= ["username","email","password1","password2"]
        help_texts ={k:"" for k in fields} #indicando que los campos de ayuda del formulario esten vacios (" ") , en ese espacio, todos son vacio por cada uno de los campos