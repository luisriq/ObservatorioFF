from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from django.utils.encoding import smart_str, smart_unicode
import json

from .models import *
ckey = 'wcBPjzyOQhZm7RhTcOqrChbWI'
csecret = 'zGTsXDVEED59MB0wpvGMD6spGYr1HYrKRG9c4CVYy9G9N3Djbl'
atoken = '228562756-PW0YtSmyS32fEwPFucXaGlkdPRP53hisP1NYoCr4'
asecret = 'yS7cOL3XD3bP6Oi2OcrOD1mWtaqpFnciEKqFhcsg7zafz'

limite = 1000
i = 0
listaCadenas = [ {"cadena":"KFC", "cuentas":[
					"kfc",
					"KFCSA",
					"KFC_UKI",
					"KFCcl",
					"kfcarabia",
					"KFCFrance",
					"kfcnederland",
					"KFC_jp",
					"KFC_SG",
					"KFC_fob"]},
			 	{"cadena":"McDonald", "cuentas":[
			 		"McDonalds",
					"McDonaldsCorp",
					"McDonaldsUK",
					"McDonalds_Ar",
					"McDonaldsArabia",
					"McDonaldsMexico",
					"McDonalds_DMV",
					"McDonaldsCol",
					"McDonalds_Ecu",
					"McDonalds_VE",
					"McDonalds_Cl",
					"McDonaldsEgypt",
					"McDonalds_PER",
					"McDonalds_Uy",
					"NebMcDonalds",
					"McDonaldsEurope",
					"McDonaldsETN"]},
			 	{"cadena":"Burger King", "cuentas":[
			 		"BurgerKing",
					"BurgerKing_ID",
					"BurgerKingMX",
					"BurgerKingFR",
					"BurgerKingBR",
					"burgerkingph",
					"BurgerKingNL"]
		 		},{"cadena":"Telepizza", "cuentas":[
		 			"TelepizzaChile",
					"telepizza",
					"telepizzalucena",
					"TelepizzaCuenca",
					"TelepizzaPt",
					"TelepizzaUAE",
					"pizzavalde",
					"TelepizzaTeruel",
					"tpantequera",
					"TelepizzaMania",
					"TELEPIZZA_LEBRI",
					"TelepizzaVilaga",
					"TelepizzaPeru",
					"TELEPIZZALALINE",
					"Yosoy_Chile",
					"TelepizzaMntq",
					"telepizza_pa",
					"MartosTelepizza",
					"telepizzajaen"]
			 	},{"cadena":"Tarragona", "cuentas":[
			 		"tarragonaChile"]
			 	},{"cadena":"Pedro juan y diego", "cuentas":[
			 		"PedroJuanDiego"]
			 	},{"cadena":"Doggis", "cuentas":[
			 		"_doggito_"]
			 	},{"cadena":"Juan maestro", "cuentas":[
			 		"JuanMaestro"]
			 	},{"cadena":"Pizza Hut", "cuentas":[
			 		"pizzahut",
					"pizzahutuk",
					"PizzaHutIN",
					"pizzahutmsia",
					"pizzahutdeliver",
					"PizzaHutME",
					"PizzaHutPak",
					"PizzaHut_SG",
					"PizzaHutCares",
					"pizzahutphils",
					"PizzaHutAus",
					"PizzaHutkuwait"]
			 	},{"cadena":"Tacobell", "cuentas":[
			 		"tacobell",
					"tacobell_cr",
					"TacoBell4Teens",
					"TacoBellCanada",
					"TacoBellTruck",
					"TacoBellTeam",
					"TacoBellSpain",
					"TacoBellGuate",
					"tacobelluk",
					"TacoBellPA"]
			 	},{"cadena":"Domino", "cuentas":[
			 		"dominomag",
					"dominos",
					"Dominos_UK",
					"Dominorecordco",
					"TheDomino",
					"Dominos_AU",
					"dominosmx",
					"DominoRecordsDE",
					"dominos_NZ"]
			 	}]

class listener(StreamListener):
	
	def __init__(self, api=None):
		super(listener, self).__init__()
		self.count = 0
		self.lista = []

	def on_status(self, status):
		if self.count < 5:
			print status
			self.count += 1
			self.lista.append(status)
			return True
		else:
			print "Fin de la busqueda"
			return False 

	def on_error(self, status):
		print status

def home(request, otro):
	l = listener()
	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	stream = Stream(auth, l)
	listaU = []
	listaH = []
	for e in listaCadenas:
		for us in e["cuentas"]:
			listaU.append("@"+us)
			listaH.append("#"+us)

	stream.filter(track=listaU+listaH)
	lista = l.lista
	api = tweepy.API(auth)
	#lista = api.search(q="kfc", count=1)
	for tweet in lista:	#tweepy.Cursor(api.search, q=('kfc')).items(20
		print "tweet : ", tweet.text
		listaHashtags = tweet.entities.get('hashtags')
		print "---------------------------------------------------------"
		print "hashtagas : ", listaHashtags
		print "---------------------------------------------------------"
		for hashtag in listaHashtags:
			cadena = ''
			for c in listaCadenas:
				for h in c["cuentas"]:
					if h == hashtag[u'text']:
						cadena = c["cadena"]
						u = api.get_user(h)
						name = u.screen_name
						segui = u.followers_count
						loc = u.location.split(",")
						city = loc[0]
						country = "Chile"
						re = tweet.retweet_count
						msg = tweet.text
						msg = smart_str(msg)
						print "Cadena :", cadena
						print "Name :", name
						print "Segui :", segui
						print "msg :", msg
						contiene = Contiene.crearContiene(hashtag[u'text'], cadena, re, msg, name, segui, city, country)

		listaUsers = tweet.entities.get('user_mentions')
		for usuario in listaUsers:
			name = ''
			for c in listaCadenas:
				for h in c["cuentas"]:
					if h == usuario[u'screen_name']:	
						u = api.get_user(usuario["screen_name"])
						cadena = c["cadena"]
						segui = u.followers_count
						loc = u.location.split(",")
						city = loc[0]
						country = "Chile"
						name = usuario[u'screen_name']
						re = tweet.retweet_count
						favs = u.favourites_count
						msg = tweet.text
						print "Json a dic :", type(usuario)
						print "Usuario :", usuario
						print name
						print "Retw :", re
						print "Favritos :", favs
						print "Texto :", msg
						mencion = Menciona.crearMenciona(re, smart_str(msg), name, segui, city, country, cadena)
						#usuario = Usuario.crearUsurio(usuario, segui, city, country)


		


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