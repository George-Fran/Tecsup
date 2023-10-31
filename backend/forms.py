from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Noticia, Evento, Proyecto, Carrera, Periodo
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'autofocus': True, 'class': 'input'}),
            'password': forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'input'}),
        }      

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'resumen', 'contenido', 'carrera', 'sede', 'image', 'image2', 'image3']

class DateInput(forms.DateInput):
    input_type = 'date'

class EventoForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Evento
        fields = ['fecha', 'titulo', 'lugar', 'descripcion', 'link', 'image']
        widgets = {
            "fecha": DateInput
        }

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'integrantes', 'asesor', 'carrera', 'ciclo', 'periodo', 'url', 'resumen', 'image', 'image2', 'image3']

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['carrera', 'abreviatura']

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['periodo']


