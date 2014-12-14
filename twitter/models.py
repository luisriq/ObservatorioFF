from django.db import models
from random import randint


class Pais(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	class Meta:
		verbose_name_plural = "Pais"
	def __unicode__(self):
		return self.nombre

	@staticmethod
	def crearPais(nombre):
		try:
			pais = Pais.objects.get(nombre=nombre)
		except:
			pais = Pais()
			pais.nombre = nombre
		pais.save()
		return pais

class Ciudad(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	id_pais = models.ForeignKey(Pais)
	class Meta:
		verbose_name_plural = "Ciudad"
	def __unicode__(self):
		return self.nombre
	@staticmethod
	def crearCiudad(nombre, pais):
		try:
			ciudad = Ciudad.objects.get(nombre=nombre)
		except:
			ciudad = Ciudad()
			ciudad.nombre = nombre
			ciudad.id_pais = Pais.crearPais(pais)
		ciudad.save()
		return ciudad


class Cadena(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	class Meta:
		verbose_name_plural = "Cadena"
	def __unicode__(self):
		return self.nombre
	@staticmethod
	def crearCadena(nombre):
		try:
			cadena = Cadena.objects.get(nombre=nombre)
		except:
			cadena = Cadena()
			cadena.nombre = nombre
		cadena.save()
		return cadena



class Usuario(models.Model):
	seguidores = models.PositiveIntegerField()
	cuenta = models.CharField(max_length = 255, default = '')
	id_ciudad = models.ForeignKey(Ciudad)
	id_cadena = models.ForeignKey(Cadena, blank=True, null = True)
	class Meta:
		verbose_name_plural = "Usuario"
	def __unicode__(self):
		return self.cuenta
	@staticmethod
	def crearUsuario(nombre, seguidores, ciudad, pais, cadena):
		try:
			usuario = Usuario.objects.get(cuenta=nombre)
		except:
			usuario = Usuario()
			usuario.cuenta = nombre
			usuario.seguidores = seguidores
			usuario.id_ciudad = Ciudad.crearCiudad(ciudad, pais)
			usuario.id_cadena = Cadena.crearCadena(cadena)
		print "Creando usuario: ", usuario.cuenta
		usuario.save()
		return usuario


class Tweet(models.Model):
	retweets = models.PositiveIntegerField()
	msg = models.CharField(max_length=255, default='')
	id_usuario = models.ForeignKey(Usuario)
	favoritos = models.PositiveIntegerField(default = 0)
	class Meta:
		verbose_name_plural = "Tweet"
	def __unicode__(self):
		return self.msg
	@staticmethod
	def crearTweet(retweets, msg, usuario, seguidores, ciudad, pais, cadena):
		try:
			tweet = Tweet.objects.get(msg= msg)
		except:
			tweet = Tweet()
			tweet.msg = msg
			tweet.retweets = retweets
			tweet.id_usuario = Usuario.crearUsuario(usuario, seguidores, ciudad, pais, cadena)
			tweet.favoritos = random.randint(0, 1000)
		tweet.save()
		return tweet


class Hashtag(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	id_cadena = models.ForeignKey(Cadena)
	class Meta:
		verbose_name_plural = "Hashtag"
	def __unicode__(self):
		return self.nombre
	@staticmethod
	def crearHashtag(nombre, cadena):
		try:
			hastag = Hashtag.objects.get(nombre = nombre)
		except:
			hastag = Hashtag()
			hastag.nombre = nombre
			hastag.id_cadena = Cadena.crearCadena(cadena)
		hastag.save()
		return hastag

			

class Comida(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	class Meta:
		verbose_name_plural = "Comida"
	def __unicode__(self):
		return self.nombre
	@staticmethod
	def crearComida(nombre):
		try:
			comida = Comida.objects.get(nombre = nombre)
		except:
			comida = Comida()
			comida.nombre = nombre
		comida.save()
		return comida


class Evento(models.Model):
	fecha = models.DateTimeField(auto_now=True)
	nombre = models.CharField(max_length = 255, default = '')
	id_ciudad = models.ForeignKey(Cadena)
	class Meta:
		verbose_name_plural = "Evento"
	def __unicode__(self):
		return self.nombre



class Contiene(models.Model):
	id_hashtag = models.ForeignKey(Hashtag)
	id_tweet = models.ForeignKey(Tweet)
	class Meta:
		verbose_name_plural = "Contiene"
	def __unicode__(self):
		return str(self.id_hashtag.nombre)
	@staticmethod
	def crearContiene(hashtag, cadena, retweets, msg, usuario, seguidores, ciudad, pais):
		_hashtag = Hashtag.crearHashtag(hashtag, cadena)
		_tweet = Tweet.crearTweet(retweets, msg, usuario, seguidores, ciudad, pais, cadena)
		try:
			contiene = Contiene.objects.get(id_hashtag = _hashtag, id_tweet = _tweet)
		except:
			contiene = Contiene()
			contiene.id_tweet = _tweet
			contiene.id_hashtag = _hashtag
		contiene.save()
		return contiene

class Menciona(models.Model):
	id_usuario = models.ForeignKey(Usuario)
	id_tweet = models.ForeignKey(Tweet)
	class Meta:
		verbose_name_plural = "Menciona"
	def __unicode__(self):
		return str(self.id_usuario.cuenta)
	@staticmethod
	def crearMenciona(retweets, msg, usuario, seguidores, ciudad, pais, cadena):
		usua = Usuario.crearUsuario(usuario, seguidores, ciudad, pais, cadena)
		tweet = Tweet.crearTweet(retweets, msg, usuario, seguidores, ciudad, pais, cadena)
		try:
			menciona = Menciona.objects.get(usua, tweet)
		except:
			menciona = Menciona()
			menciona.id_usuario=usua
			menciona.id_tweet = tweet
		menciona.save()
		return menciona

class Referencia(models.Model):
	id_comida = models.ForeignKey(Comida)
	id_hashtag = models.ForeignKey(Hashtag)
	class Meta:
		verbose_name_plural = "Referencia"
	def __unicode__(self):
		return self.nombre



class Sigue(models.Model):
	id_cadena = models.ForeignKey(Cadena)
	id_usuario = models.ForeignKey(Usuario)
	class Meta:
		verbose_name_plural = "Sigue"
	def __unicode__(self):
		return str(self.id_cadena.nombre)
	@staticmethod
	def crearSigue(usuario, seguidores, ciudad, pais, cadena):
		_cadena = Cadena.crearCadena(cadena)
		_usuario = Usuario.crearUsuario(usuario, seguidres, ciudad, pais)
		try:
			sigue = Sigue.objects.get(id_cadena = _cadena, id_usuario=_usuario)
		except:
			sigue = Sigue()
			sigue.id_cadena = _cadena
			sigue.id_usuario = _usuario
		sigue.save()
		return sigue


class Prepara(models.Model):
	id_comida = models.ForeignKey(Comida)
	id_cadena = models.ForeignKey(Cadena)
	class Meta:
		verbose_name_plural = "Prepara"
	def __unicode__(self):
		return self.nombre