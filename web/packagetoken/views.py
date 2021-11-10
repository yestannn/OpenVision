from django.shortcuts import render,redirect

from django.core import serializers
from django.http import HttpResponse
from .models import PackageToken




def tokens(request):
	jtokens = serializers.serialize("json", PackageToken.objects.all())
	return HttpResponse(jtokens, content_type="text/json-comment-filtered")