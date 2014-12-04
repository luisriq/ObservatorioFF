from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from .models import Tweet
ckey = 'wcBPjzyOQhZm7RhTcOqrChbWI'
csecret = 'zGTsXDVEED59MB0wpvGMD6spGYr1HYrKRG9c4CVYy9G9N3Djbl'
atoken = '228562756-PW0YtSmyS32fEwPFucXaGlkdPRP53hisP1NYoCr4'
asecret = 'yS7cOL3XD3bP6Oi2OcrOD1mWtaqpFnciEKqFhcsg7zafz'
class listener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

def home(request, otro):
	#auth = OAuthHandler(ckey, csecret)
	#auth.set_access_token(atoken, asecret)
	#twitterStream = Stream(auth, listener())
	#twitterStream.filter(track=["pizza"])
	return HttpResponse("ksdjhfk")#aca yo deberia estar recibiendo un json con la wea y la wea