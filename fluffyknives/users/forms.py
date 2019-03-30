from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm): # inherits from built-in Django form
	email = forms.EmailField() # required=true as default

	# form configuration
	class Meta: 
		# indication of the model that will be affected i.e. by .save()
		model = User # built-in Django model
		# specifies fields in the order that will be shown in the form
		fields = ['username', 'email', 'password1', 'password2']
		labels = {
            'username': ('Nazwa użytkownika'),
            'email': ('Emaill'),
            'password1': ('Hasło'),
            'password2': ('Potwierdź hasło'),
        }