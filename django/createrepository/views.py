from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
@login_required
def index(request):
	userDir = "/home/git/" + request.user.username
	dirContents = os.listdir(userDir)
	dirContents = [item for item in dirContents if not item.startswith(".")]

	return render(request, "createrepository/index.html", {'dirContents': dirContents})

# This should probably be converted to a simple function and be called via ajax
def createNewRepository(request):
	home = request.POST.get('home')
	projectName = request.POST.get('projectName')
	initPath = "git init --bare " + home + "/" + projectName + ".git"
	os.system(initPath)
	
	dirContents = os.listdir("/home/git/")
	dirContents = [item for item in dirContents if not item.startswith(".")]

	return render(request, "createrepository/index.html", {'dirContents': dirContents})