from django.shortcuts import render
import os

# Create your views here.

def index(request):

	return render(request, "repository/index.html")