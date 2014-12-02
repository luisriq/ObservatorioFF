from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Tweet
def home(request):
	return HttpResponse("Hola mundo!!!!")
def home(request, otro):
	res = "<!DOCTYPE html>"+"<html>"+"<body>"
	res += "<table border=\"2\" style=\"width:100%\">"
	res += "<tr><td>msg</td><td>retweets</td><td>favs</td>"
	for t in Tweet.objects.all():
		res += "<tr><td>"+t.msg+"</td>"+"<td>%d</td>" % t.favs+"<td>%d</td>" % (t.retweets)+"</tr>"
	res += "</table>"
	res += "</body>"+"</html>"
	return HttpResponse(res+"<br />Hola mundo!!!!")

