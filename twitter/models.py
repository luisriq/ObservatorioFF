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
			ciudad.id_pais = pais



class Usuario(models.Model):
	seguidores = models.PositiveIntegerField()
	cuenta = models.CharField(max_length = 255, default = '')
	id_ciudad = models.ForeignKey(Ciudad)
	class Meta:
		verbose_name_plural = "Usuario"
	def __unicode__(self):
		return self.cuenta

	def crearUsuario(nombre, ciudad):
		try:
			usuario = Usuario.objects.get(nombre)
			return usuario
		except:
			usuario = Usuario()
			usuario.nombre = nombre
			usuario.id_ciudad = ciudad
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

class Cadena(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	class Meta:
		verbose_name_plural = "Cadena"
	def __unicode__(self):
		return self.nombre

class Hashtag(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	id_cadena = models.ForeignKey(Cadena)
	class Meta:
		verbose_name_plural = "Hashtag"
	def __unicode__(self):
		return self.nombre

class Comida(models.Model):
	nombre = models.CharField(max_length = 255, default = '')
	class Meta:
		verbose_name_plural = "Comida"
	def __unicode__(self):
		return self.nombre


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

class Menciona(models.Model):
	id_usuario = models.ForeignKey(Usuario)
	id_tweet = models.ForeignKey(Tweet)
	class Meta:
		verbose_name_plural = "Menciona"
	def __unicode__(self):
		return self.nombre

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