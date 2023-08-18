from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", max_length=50)
    password = forms.CharField(label="Contraseña", max_length=100, widget=forms.PasswordInput())