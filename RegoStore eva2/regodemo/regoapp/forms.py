from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')  # Campo para el correo electrónico

    class Meta:
        model = User  # Modelo de usuario de Django
        fields = ['username', 'email', 'password1', 'password2']  # Campos a incluir en el formulario
        labels = {
            'username': 'Nombre de Usuario'  # Etiqueta personalizada para el campo de nombre de usuario
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User  # Modelo de usuario de Django
        fields = ['username', 'email']  # Campos que se pueden actualizar
