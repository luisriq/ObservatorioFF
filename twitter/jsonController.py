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
def menciones():
	#cargar aqui datos de menciones.
	""" Formato
	[{
        \"value\": <cantidad:int>,
        \"color\":\"#F7464A\",#color representativo
        \"highlight\": \"#FF5A5E\",#deberia ser el mismo mas clarito
        \"label\": \"Nombre de la cadena\"
    },...]
	"""
	jsonMenciones='[{\"value\": 300,\"color\":\"#F7464A\",\"highlight\": \"#FF5A5E\",\"label\": \"McDonals\"},{\"value\": 150,\"color\": \"#46BFBD\",\"highlight\": \"#5AD3D1\",\"label\": \"Burger King\"},{\"value\": 100,\"color\": \"#FDB45C\",\"highlight\": \"#FFC870\",\"label\": \"KFC\"}]'
	return jsonMenciones
def favoritos():
	#cargar aqui datos de menciones.
	""" Formato
	{
            \"labels\": [\"Eating\", \"Drinking\", \"Sleeping\", \"Designing\", \"Coding\", \"Cycling\", \"Running\"],
            \"datasets\": [
              {
                \"label\": \"My First dataset\",
                \"fillColor\": \"rgba(230,165,0,0.5)\",
                \"strokeColor\": \"rgba(230,165,0,.8)\",
                \"pointColor\": \"rgba(250,110,0,1)\",
                \"pointStrokeColor\": \"#fff\",
                \"pointHighlightFill\": \"#fff\",
                \"pointHighlightStroke\": \"rgba(220,220,220,1)\",
                \"data\": [65,59,90,81,56,55,40]
              }
            ]
          }
	"""
	jsonMenciones='{ \"labels\": ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"], \"datasets\": [{ \"label\": \"My First dataset\",\"fillColor\": \"rgba(230,165,0,0.5)\",\"strokeColor\": \"rgba(230,165,0,.8)\",\"pointColor\": \"rgba(250,110,0,1)\",\"pointStrokeColor\": \"#fff\",\"pointHighlightFill\": \"#fff\",\"pointHighlightStroke\": \"rgba(220,220,220,1)\",\"data\": [65,59,90,81,56,55,40]}]}'
	return jsonMenciones
def favoritos():
	#cargar aqui datos de menciones.
	""" Formato
	{
            \"labels\": [\"Eating\", \"Drinking\", \"Sleeping\", \"Designing\", \"Coding\", \"Cycling\", \"Running\"],
            \"datasets\": [
              {
                \"label\": \"My First dataset\",
                \"fillColor\": \"rgba(230,165,0,0.5)\",
                \"strokeColor\": \"rgba(230,165,0,.8)\",
                \"pointColor\": \"rgba(250,110,0,1)\",
                \"pointStrokeColor\": \"#fff\",
                \"pointHighlightFill\": \"#fff\",
                \"pointHighlightStroke\": \"rgba(220,220,220,1)\",
                \"data\": [65,59,90,81,56,55,40]
              }
            ]
          }
	"""
	jsonMenciones='{ \"labels\": ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"], \"datasets\": [{ \"label\": \"My First dataset\",\"fillColor\": \"rgba(230,165,0,0.5)\",\"strokeColor\": \"rgba(230,165,0,.8)\",\"pointColor\": \"rgba(250,110,0,1)\",\"pointStrokeColor\": \"#fff\",\"pointHighlightFill\": \"#fff\",\"pointHighlightStroke\": \"rgba(220,220,220,1)\",\"data\": [65,59,90,81,56,55,40]}]}'
	return jsonMenciones
def home(request, otro):
	respuesta = "Error de Soicitud"
	if(otro=="menciones"):
		respuesta=menciones()
	if(otro=="favoritos"):
		respuesta=favoritos()
	#auth = OAuthHandler(ckey, csecret)
	#auth.set_access_token(atoken, asecret)
	#twitterStream = Stream(auth, listener())
	#twitterStream.filter(track=["pizza"])
	return HttpResponse(respuesta)#aca yo deberia estar recibiendo un json con la wea y la wea
def tweets(request, otro):
	lista = []
	for t in Tweet.objects.all():
		lista.append([t.id_usuario.cuenta, t.msg])

	return render(request, 'template.html', {'tweets':lista})
