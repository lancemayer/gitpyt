from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import os, getpass

def index(request):

 	return render(request, "gitpyt/index.html")

def mkdir(request):
	home = "~"
	projectName = "proj4.git"
	initPath = "git init --bare " + home + "/" + projectName
	# os.system(initPath)
	# print(getpass.getuser())

	return render(request, "gitpyt/mkdir.html")