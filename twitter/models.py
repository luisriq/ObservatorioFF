from django.db import models

class Tweet(models.Model):
	retweets = models.PositiveIntegerField()
	favs = models.PositiveIntegerField()
	msg = models.CharField(max_length=255, default='')
	def __unicode__(self):
		return self.msg