from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

def index(request):

 	return render(request, "gitpyt/index.html")