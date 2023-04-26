from django import forms


class Profesorform(forms.Form):
    nombre = forms.CharField(max_length=30, label="Nombre del profesor")
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profecion = forms.CharField(max_length=30)


class Estudiantesform(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellitod = forms.CharField(max_length=30)
    email = forms.EmailField()