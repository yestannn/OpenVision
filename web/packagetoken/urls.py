from django.urls import path
from packagetoken import views

urlpatterns = [
    path('tokens/', views.tokens, name='tokens')
]