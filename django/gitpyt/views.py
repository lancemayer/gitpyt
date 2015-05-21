from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import os, getpass

def index(request):

 	return render(request, "gitpyt/index.html")

def loginPage(request):

	return render(request, "gitpyt/login.html")

def authenticateUser(request):
	if request.method == "POST":
		if request.user.is_authenticated() == False:
			return authenticateAndLoginUserInternal(request)
		else:
			#already logged in
			return redirect('/')

def authenticateAndLoginUserInternal(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(username = username, password = password)
	if user is not None:
		login(request, user)
		return redirect('/')
	else:
		return HttpResponse("login failed")

def logoutUser(request):
	logout(request)
	
	return redirect('/')

def signup(request):
	if request.method == 'POST':
		firstName = request.POST["firstName"]
		lastName = request.POST["lastName"]
		username = request.POST["username"]
		password = request.POST["password"]
		user = User.objects.create_user(username = username, password = password, first_name = firstName, last_name = lastName)

		user.save()

		return render(request, "gitpyt/login.html")

	return render(request, "gitpyt/signup.html")