from django.urls import path
from django.views.decorators.http import  require_POST
from . import views

urlpatterns = [
    path('', views.home, name='packages-base'),
]