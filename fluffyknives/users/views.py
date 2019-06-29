from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save() # saves to the db; automaticaly hashes passwords
			return render(request, 'users/register_ok.html')
	else:
		form = UserRegisterForm()
	# if form is not valid - form renders again with previous data (form=form from 'if POST' block)
	return render(request, 'users/register.html', {'form': form})
	