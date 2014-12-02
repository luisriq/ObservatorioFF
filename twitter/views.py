from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Tweet
def home(request):
	return HttpResponse("Hola mundo!!!!")
def home(request, otro):
	res = ""
	res += "|msg\t|retweets\t|favs"
	for t in Tweet.objects.all():
		res += "<br />"+t.msg+"\t"+"%d" % t.favs+"\t%d" % (t.retweets) 
	
	if(str(otro).isdigit()):
		return HttpResponse(res+"<br />Hola %d mundo!!!!" % int(otro))
	else:
		return HttpResponse(res+"<br />Hola mundo!!!! no muneros"+str(otro)+str(tweet.msg))
