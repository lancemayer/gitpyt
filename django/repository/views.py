from django.shortcuts import render
import os, subprocess

# Create your views here.

def index(request, repoName):
	userDir = "/home/git/" + request.user.username
	repoPath = userDir + "/" + repoName
	branch = "master"
	repoContents = []

	# Changes directory to the selelcted repo and gets files for selected branch
	command = "cd " + repoPath + " && git ls-tree --full-tree -r --name-only " + branch

	repoList = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(out, err) = repoList.communicate()

	# Converts byte string to utf-8 characters
	out = out.decode("utf-8")

	# Splits string at new line character and appends each part to the files list
	for x in out.split("\n"):
		repoContents.append(x)

	return render(request, "repository/index.html", {'repoName': repoName,
														'contents': repoContents})