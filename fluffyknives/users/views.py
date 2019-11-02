from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



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



@login_required
def profile(request):
	if request.user.is_superuser:
		return redirect('shop-main')

	if request.method == 'POST':
		userForm = UserUpdateForm(request.POST, instance=request.user) # request.POST - gets posted data, instance set to specify which user to update
		profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		
		if userForm.is_valid() and profileForm.is_valid():
			userForm.save()
			profileForm.save()
			return render(request, 'users/updated.html')

	else:
		userForm = UserUpdateForm(instance=request.user) # instance=request.user - fills form fields by current user data
		profileForm = ProfileUpdateForm(instance=request.user.profile)
		context = {
			'userForm': userForm,
			'profileForm': profileForm
		}
	return render(request, 'users/profile.html', context)
