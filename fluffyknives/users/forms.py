from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
                    'username': ('Nazwa użytkownika'),
                    'email': ('Emaill'),
                    'password1': ('Hasło'),
                    'password2': ('Potwierdź hasło'),
                }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'email']
        labels = {
                    'username': ('Nazwa użytkownika'),
                    'email': ('Emaill'),
                }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'adress', 'phone']
        labels = {
                    'image': ('Zaktualizuj zdjęcie profilowe'),
                    'adress': ('Adres'),
                    'phone': ('Numer telefonu'),
                }