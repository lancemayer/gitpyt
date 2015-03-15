from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

def index(request):
	# template = loader.get_template('gitpyt/index.html')
 	#context = RequestContext(request)
 	print("Index")

 	# return HttpResponse("Hello gitpy")
 	return render(request, "gitpyt/index.html")