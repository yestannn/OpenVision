from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'base/home.html')

def custom_permission_denied_view(request, exception=None):
	return render(request, "errors/403.html")