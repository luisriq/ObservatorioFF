from django.db import models


class Pais(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	class Meta:
		verbose_name_plural = "Pais"
	def __unicode__(self):
		return self.nombre

	@staticmethod
	def crearPais(nombre):
		try:
			pais = Pais.objects.get(nombre)
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
			ciudad = Ciudad.objects.get(nombre)
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
	def crearCadena(nombre, usuario):
		try:
			cadena = Cadena.objects.get(nombre=nombre, id_usuario=usuario)
		except:
			cadena = Cadena()
			cadena.nombre = nombre
		cadena.save()
		return cadena



class Usuario(models.Model):
	seguidores = models.PositiveIntegerField()
	cuenta = models.CharField(max_length = 255, default = '')
	id_ciudad = models.ForeignKey(Ciudad)
	id_cadena = models.ForeignKey(Cadena, null=True)
	class Meta:
		verbose_name_plural = "Usuario"
	def __unicode__(self):
		return self.cuenta
	@staticmethod
	def crearUsuario(nombre, seguidores, ciudad, pais):
		try:
			usuario = Usuario.objects.get(nombre)
		except:
			usuario = Usuario()
			usuario.nombre = nombre
			usuario.seguidores = seguidores
			usuario.id_ciudad = Ciudad.crearCiudad(ciudad, pais)
		usuario.save()
		return usuario


class Tweet(models.Model):
	retweets = models.PositiveIntegerField()
	msg = models.CharField(max_length=255, default='')
	id_usuario = models.ForeignKey(Usuario)
	class Meta:
		verbose_name_plural = "Tweet"
	def __unicode__(self):
		return self.msg
	@staticmethod
	def crearTweet(retweets, msg, usuario, seguidores, ciudad, pais):
		try:
			tweet = Tweet.objects.get(msg)
		except:
			tweet = Tweet()
			tweet.msg = msg
			tweet.retweets = retweets
			tweet.id_usuario = Usuario.crearUsuario(usuario, seguidores, ciudad, pais)
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
			hastag = Hashtag.objects.get(nombre)
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
			comida = Comida.objects.get(nombre)
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
		return str(self.id_hashtag.nombre) + "," + str(self.id_tweet.msg)
	@staticmethod
	def crearContiene(hashtag, cadena, retweets, msg, usuario, seguidores, ciudad, pais):
		try:
			contiene = Contiene.objects.get(str(hashtag)+","+str(msg))
		except:
			contiene = Contiene()
			contiene.id_hashtag = Hashtag.crearHashtag(hastag, cadena)
			contiene.id_tweet = Tweet.crearTweet(retweets, msg, usuario, seguidores, ciudad, pais)
		contiene.save()
		return contiene

class Menciona(models.Model):
	id_usuario = models.ForeignKey(Usuario)
	id_tweet = models.ForeignKey(Tweet)
	class Meta:
		verbose_name_plural = "Menciona"
	def __unicode__(self):
		return str(self.id_usuario.cuenta)+","+str(self.id_tweet.msg)
	@staticmethod
	def crearMenciona(retweets, msg, usuario, seguidores, ciudad, pais):
		try:
			menciona = Menciona.objects.get(usuario+","+msg)
		except:
			menciona = Menciona()
			menciona.id_usuario = Usuario.crearUsuario(usuario, seguidores, ciudad, pais)
			menciona.id_tweet = Tweet.crearTweet(retweets, msg, usuario, seguidores, pais, ciudad)
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
		return str(self.id_cadena.nombre)+","+str(self.id_usuario.nombre)
	@staticmethod
	def crearSigue(usuario, seguidores, ciudad, pais, cadena):
		try:
			sigue = Sigue.objects.get(cadena+","+usuario)
		except:
			sigue = Sigue()
			sigue.id_cadena = Cadena.crearCadena(cadena)
			sigue.id_usuario = Usuario.crearUsuario(usuario, seguidres, ciudad, pais)
		sigue.save()
		return sigue


class Prepara(models.Model):
	id_comida = models.ForeignKey(Comida)
	id_cadena = models.ForeignKey(Cadena)
	class Meta:
		verbose_name_plural = "Prepara"
	def __unicode__(self):
		return self.nombre