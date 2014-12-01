from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("Hola mundo!!!!")
def home(request, otro):
	if(str(otro).isdigit()):
		return HttpResponse("Hola %d mundo!!!!" % int(otro))
	else:
		return HttpResponse("Hola mundo!!!! no muneros"+str(otro))
