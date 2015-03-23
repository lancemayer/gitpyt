from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import os, getpass

def index(request):

 	return render(request, "gitpyt/index.html")

def mkdir(request):
	initPath = "git init --bare /home/" + getpass.getuser() + "/proj2.git"
	# os.system("git init --bare /home/git/proj.git")
	os.system(initPath)
	# print(getpass.getuser())

	return render(request, "gitpyt/mkdir.html")