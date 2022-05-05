from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth.models import User

from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.

def get_or_create_profile(request):
	obj, created = Profile.objects.get_or_create(user=request.user, defaults={'user':request.user})
	if created:
		obj.save()
	return obj

@login_required
def profile(request):
	profile = get_or_create_profile(request)
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
								   instance=profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'User profile updated')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=profile)

	context = {
		'u_form': u_form,
		'p_form': p_form,
	}

	return render(request, 'user/profile.html', context)

