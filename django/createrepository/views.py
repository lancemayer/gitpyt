from django.shortcuts import render
import os

# Create your views here.
def index(request):
	dirContents = os.listdir("/home/git/")
	dirContents = [item for item in dirContents if not item.startswith(".")]

	return render(request, "createrepository/index.html", {'dirContents': dirContents})

# This should probably be converted to a simple function 
def createNewRepository(request):
	home = request.POST.get('home')
	projectName = request.POST.get('projectName')
	initPath = "git init --bare " + home + "/" + projectName +".git"
	os.system(initPath)
	
	dirContents = os.listdir("/home/git/")
	dirContents = [item for item in dirContents if not item.startswith(".")]

	return render(request, "createrepository/index.html", {'dirContents': dirContents})