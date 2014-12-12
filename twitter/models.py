from django.db import models


class Pais(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	class Meta:
		verbose_name_plural = "Pais"
	def __unicode__(self):
		return self.nombre

	def crearPais(nombre):
		try:
			pais = pais.objects.get(nombre)
		except:
			pais = pais()
			pais.nombre = nombre
		return pais

class Ciudad(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	id_pais = models.ForeignKey(Pais)
	class Meta:
		verbose_name_plural = "Ciudad"
	def __unicode__(self):
		return self.nombre
	
	def crearCiudad(nombre, pais):
		try:
			ciudad = Ciudad.objects.get(nombre)
		except:
			ciudad = Ciudad()
			ciudad.nombre = nombre
			ciudad.id_pais = Pais.crearPais(pais)
		return ciudad



class Usuario(models.Model):
	seguidores = models.PositiveIntegerField()
	cuenta = models.CharField(max_length = 255, default = '')
	id_ciudad = models.ForeignKey(Ciudad)
	class Meta:
		verbose_name_plural = "Usuario"
	def __unicode__(self):
		return self.cuenta

	def crearUsuario(nombre, ciudad, pais):
		try:
			usuario = Usuario.objects.get(nombre)
		except:
			usuario = Usuario()
			usuario.nombre = nombre
			usuario.id_ciudad = Ciudad.crearCiudad(ciudad, pais)
		return usuario


class Tweet(models.Model):
	retweets = models.PositiveIntegerField()
	favs = models.PositiveIntegerField()
	msg = models.CharField(max_length=255, default='')
	id_usuario = models.ForeignKey(Usuario)
	class Meta:
		verbose_name_plural = "Tweet"
	def __unicode__(self):
		return self.msg

	def crearTweet(retweets, favs, msg, usuario, pais, ciudad):
		try:
			tweet = Tweet.objects.get(msg)
		except:
			tweet = Tweet()
			tweet.msg = msg
			tweet.retweets = retweets
			tweet.favs = favs
			tweet.id_usuario = Usuario.crearUsuario(usuario, ciudad, pais)
		return tweet

class Cadena(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	class Meta:
		verbose_name_plural = "Cadena"
	def __unicode__(self):
		return self.nombre

	def crearCadena(nombre):
		try:
			cadena = Cadena.objects.get(msg)
		except:
			cadena = Cadena()
			cadena.nombre = nombre
		return tweet

class Hashtag(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	id_cadena = models.ForeignKey(Cadena)
	class Meta:
		verbose_name_plural = "Hashtag"
	def __unicode__(self):
		return self.nombre

	def crearHashtag(nombre, cadena):
		try:
			hastag = Hashtag.objects.get(nombre)
		except:
			hastag = Hashtag()
			hastag.nombre = nombre
			hastag.id_cadena = Cadena.crearCadena(cadena)
		return hastag

			

class Comida(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	class Meta:
		verbose_name_plural = "Comida"
	def __unicode__(self):
		return self.nombre

	def crearComida(nombre):
		try:
			comida = Comida.objects.get(nombre)
		except:
			comida = Comida()
			comida.nombre = nombre
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
		return self.nombre

	def crearContiene(hashtag, tweet, cadena, retweets, favs, msg, usuario, pais, ciudad):
		try:
			contiene = Contiene.objects.get(nombre)
		except:
			contiene = Contiene()
			contiene.id_hashtag = Hashtag.crearHashtag(hastag, cadena)
			contiene.id_tweet = Tweet.crearTweet(retweets, favs, msg, usuario, pais, ciudad)
		return contiene

class Menciona(models.Model):
	id_usuario = models.ForeignKey(Usuario)
	id_tweet = models.ForeignKey(Tweet)
	class Meta:
		verbose_name_plural = "Menciona"
	def __unicode__(self):
		return self.nombre

	def crearMenciona(usuario, pais, ciudad, retweets, favs, msg):
		try:
			menciona = Menciona.objects.get(nombre)
		except:
			menciona = Menciona()
			menciona.id_usuario = Usuario.crearUsuario(usuario, pais, ciudad)
			menciona.id_tweet = Tweet.crearTweet(retweets, favs, msg, usuario, pais, ciudad)
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
		return self.nombre

	def crearSigue(usuario, pais, ciudad, retweets, favs, msg):
		try:
			sigue = Sigue.objects.get(nombre)
		except:
			sigue = Sigue()
			sigue.id_cadena = Cadena.crearCadena(usuario, pais, ciudad)
			sigue.id_usuario = Usuario.crearUsuario(retweets, favs, msg, usuario, pais, ciudad)
		return sigue

class Representa(models.Model):
	id_cadena = models.ForeignKey(Cadena)
	id_usuario = models.ForeignKey(Usuario)
	class Meta:
		verbose_name_plural = "Representa"
	def __unicode__(self):
		return self.nombre


class Prepara(models.Model):
	id_comida = models.ForeignKey(Comida)
	id_cadena = models.ForeignKey(Cadena)
	class Meta:
		verbose_name_plural = "Prepara"
	def __unicode__(self):
		return self.nombre