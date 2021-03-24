from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'post': 'Home page'
        }

    return render(request, 'packages/home.html', context)