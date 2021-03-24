from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('packages-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
