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
	# context must be given as library type
	return render(request, 'users/register.html', {'form': form})
	