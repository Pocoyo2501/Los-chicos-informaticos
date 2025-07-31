from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Login por correo
class EmailLoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Correo no registrado.")

            user = authenticate(username=user.username, password=password)
            if not user:
                raise forms.ValidationError("Contraseña incorrecta.")

            cleaned_data['user'] = user
        return cleaned_data


# Registro de usuario
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
