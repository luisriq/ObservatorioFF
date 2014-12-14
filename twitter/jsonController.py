from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from random import shuffle
import json
from .models import *
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
	
	datos = {}
	for cad in Cadena.objects.all():
		try:
			datos[cad.nombre] = 0
			for user in Usuario.objects.filter(id_cadena = cad):
				datos[cad.nombre] = datos[cad.nombre] + len(Menciona.objects.filter(id_usuario=user))
				print datos
		except:
			print "no"
	print "datosadsd",datos
	jsonMenciones=" ["
	print type(jsonMenciones)
	js = []

	normal=["#F00","#F90","#FF0","#CF0","#2F2","#2F9","#0FF","#09F","#00F","#70F","#F90","#FF0","#CF0","#2F2","#2F9","#0FF","#09F","#00F","#70F"]
	highlight=["#F33","#FA3","#FF5","#DF2","#5F5","#5FB","#5FF","#3BF","#33F","#B3F","#FA3","#FF5","#DF2","#5F5","#5FB","#5FF","#3BF","#33F","#B3F"]
	c=0
	for k in datos.keys():
		c+=1
		print k, datos[k]
		print type(jsonMenciones)
		js.append({"value":datos[k],"color": normal[c], "highlight": highlight[c],"label": k})
	return json.dumps(js)
def favoritos():
	#cargar aqui datos de menciones.
	cadenas = []
	contadores = []
	for cad in Cadena.objects.all():
		cadenas.append(cad.nombre)
		cont = 0
		for user in Usuario.objects.filter(id_cadena=cad):
			for men in Menciona.objects.filter(id_usuario=user):
				cont += men.id_tweet.favoritos
		contadores.append(cont)
	print cadenas,"|",contadores

	js = {
		"labels": cadenas,
		"datasets": [
		{"label": "Favoritos",
			"fillColor": "rgba(230,165,0,0.5)",
    	    "strokeColor": "rgba(230,165,0,.8)",
        	"pointColor": "rgba(250,110,0,1)",
	        "pointStrokeColor": "#fff",
	        "pointHighlightFill": "#fff",
	        "pointHighlightStroke": "rgba(220,220,220,1)",
	        "data": contadores
            }
		]
	}
	jsonMenciones='{ \"labels\": ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"], \"datasets\": [{ \"label\": \"My First dataset\",\"fillColor\": \"rgba(230,165,0,0.5)\",\"strokeColor\": \"rgba(230,165,0,.8)\",\"pointColor\": \"rgba(250,110,0,1)\",\"pointStrokeColor\": \"#fff\",\"pointHighlightFill\": \"#fff\",\"pointHighlightStroke\": \"rgba(220,220,220,1)\",\"data\": [65,59,90,81,56,55,40]}]}'
	print json.dumps(js)
	return json.dumps(js)
def seguidores():
	#cargar aqui datos de menciones.
	cadenas = []
	contadores = []
	for cad in Cadena.objects.all():
		cadenas.append(cad.nombre)
		cont = 0
		for user in Usuario.objects.filter(id_cadena=cad):
			cont += user.seguidores
		contadores.append(cont)
	print cadenas,"|",contadores

	js = {
		"labels": cadenas,
		"datasets": [
		{"label": "Favoritos",
			"fillColor": "rgba(230,165,0,0.5)",
    	    "strokeColor": "rgba(230,165,0,.8)",
        	"pointColor": "rgba(250,110,0,1)",
	        "pointStrokeColor": "#fff",
	        "pointHighlightFill": "#fff",
	        "pointHighlightStroke": "rgba(220,220,220,1)",
	        "data": contadores
            }
		]
	}

	jsonMenciones='{ \"labels\": ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"], \"datasets\": [{ \"label\": \"My First dataset\",\"fillColor\": \"rgba(230,165,0,0.5)\",\"strokeColor\": \"rgba(230,165,0,.8)\",\"pointColor\": \"rgba(250,110,0,1)\",\"pointStrokeColor\": \"#fff\",\"pointHighlightFill\": \"#fff\",\"pointHighlightStroke\": \"rgba(220,220,220,1)\",\"data\": [65,59,90,81,56,55,40]}]}'
	return json.dumps(js)
def home(request, otro):
	respuesta = "Error de Soicitud"
	if(otro=="menciones"):
		respuesta=menciones()
	if(otro=="favoritos"):
		respuesta=favoritos()
	if(otro=="seguidores"):
		respuesta=seguidores()
	#auth = OAuthHandler(ckey, csecret)
	#auth.set_access_token(atoken, asecret)
	#twitterStream = Stream(auth, listener())
	#twitterStream.filter(track=["pizza"])
	return HttpResponse(respuesta)#aca yo deberia estar recibiendo un json con la wea y la wea
def tweets(request, otro):
	listaO = []
	for t in Tweet.objects.all():
		listaO.append([t.id_usuario.cuenta, t.msg])
	shuffle(listaO)
	lista = []
	i=0
	for t in listaO:
		if(i>5):
			break
		lista.append(t)
		i+=1


	return render(request, 'template.html', {'tweets':lista})
