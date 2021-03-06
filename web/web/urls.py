"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Open Vision Admin Page'
admin.site.site_title = 'Open Vision Admin Page'
admin.site.index_title = 'Open Vision Admin Page'

urlpatterns = [
    path('admin/', admin.site.urls), 
] 

urlpatterns +=  [
    path('', include('base.urls')),
    path('token/', include('packagetoken.urls')),
    path('accounts/', include('allauth.urls')),
    path('user/', include('user.urls')),
    path('team/', include('team.urls')),
]

handler403 = 'base.views.custom_permission_denied_view'
