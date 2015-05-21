from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
@login_required
def index(request):
	if request.method == "POST":
		projectName = request.POST.get('projectName')
		username = request.user.username
		createNewRepository(projectName, username)
	userDir = "/home/git/" + request.user.username
	dirContents = os.listdir(userDir)
	dirContents = [item for item in dirContents if not item.startswith(".")]

	return render(request, "createrepository/index.html", {'dirContents': dirContents})

# This should probably be called via ajax
def createNewRepository(projectName, username):
	userDir = "/home/git/" + username

	initPath = "git init --bare " + userDir + "/" + projectName + ".git"
	os.system(initPath)