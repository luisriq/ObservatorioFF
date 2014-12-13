from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from .models import Menciona, Cadena, Representa, Usuario
#xpath //ol/li/div[1]/div[2]/div[1]/a/span[2]

ckey = 'wcBPjzyOQhZm7RhTcOqrChbWI'
csecret = 'zGTsXDVEED59MB0wpvGMD6spGYr1HYrKRG9c4CVYy9G9N3Djbl'
atoken = '228562756-PW0YtSmyS32fEwPFucXaGlkdPRP53hisP1NYoCr4'
asecret = 'yS7cOL3XD3bP6Oi2OcrOD1mWtaqpFnciEKqFhcsg7zafz'

def rellenar(request, otro):
	cadenas = [ {"cadena":"KFC", "cuentas":[
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
			 	},{"cadena":"Domino", "cuentas":["dominomag",
					"dominos",
					"Dominos_UK",
					"Dominorecordco",
					"TheDomino",
					"Dominos_AU",
					"dominosmx",
					"DominoRecordsDE",
					"dominos_NZ"]
			 	}]
	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	api = tweepy.API(auth)

	for ca in cadenas:
		print "->",ca["cadena"]
		chain = Cadena()
		chain.nombre = ca["cadena"]
		chain.save()
		for cu in ca["cuentas"]:
			usu = api.get_user(screen_name = cu)
			u = Usuario.crearUsuario(cu, "Internet", "Internet")
			u.save()
			r = Representa
			r.id_cadena = chain
			r.id_usuario = u
			r.save()	 
	return HttpResponse(json.dumps(cadenas))		 
