from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import os

def index(request):

 	return render(request, "gitpyt/index.html")

def mkdir(request):
	os.system("git init --bare /home/git/proj.git")

	return render(request, "gitpyt/mkdir.html")