from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from .models import Tweet
ckey = 'wcBPjzyOQhZm7RhTcOqrChbWI'
csecret = 'zGTsXDVEED59MB0wpvGMD6spGYr1HYrKRG9c4CVYy9G9N3Djbl'
atoken = '228562756-PW0YtSmyS32fEwPFucXaGlkdPRP53hisP1NYoCr4'
asecret = 'yS7cOL3XD3bP6Oi2OcrOD1mWtaqpFnciEKqFhcsg7zafz'

limite = 1000
i = 0

class listener(StreamListener):

    def on_data(self, data):
        
        print data
        return True

    def on_error(self, status):
        print status

def home(request, otro):
	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	api = tweepy.API(auth)
	lista = api.search(q="kfc", count=100000)

	i=range(999)
	if(otro=="lawea"):
		return render(request, 'template.html', {'lista':lista})
	else:
		return render(request, 'template.html', {'lista':lista})
def homel(request, otro):
	#auth = OAuthHandler(ckey, csecret)
	#auth.set_access_token(atoken, asecret)
	#twitterStream = Stream(auth, listener())
	#twitterStream.filter(track=["pizza"])
	i=range(13)
	if(otro=="lawea"):
		return render(request, 'template.html', {'lista':i})
	else:
		return render(request, 'template.html', {'lista':range(9)})