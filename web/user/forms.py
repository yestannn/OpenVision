import django
from django import forms

from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'type': 'text',
        'name': 'first_name',
        'id': 'first-name-column'
        }))

    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'type': 'text',
        'name': 'last_name',
        'id': 'last-name-column'
        }))

    class Meta:
        model = User
        fields = [ 'first_name','last_name' ]

class ProfileUpdateForm(forms.ModelForm):
    
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Location',
        'type': 'text',
        'name': 'location',
        'id': 'city-column'
        }))

    status = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Status (member/devoleper)',
        'type': 'text',
        'name': 'status',
        'id': 'country-floating'
        }))

    class Meta:
        model = Profile
        fields = ['location', 'status']

