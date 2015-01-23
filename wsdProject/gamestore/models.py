from django.contrib.auth.models import User
from django.db import models

class Usertypes(models.Model):
	user = models.OneToOneField(User)
	usertype = models.TextField()                   

	def __unicode__(self):
		return self.user_name

class Games(models.Model):
	name = models.CharField(max_length=100, unique=True)
	category = models.CharField(max_length=100)
	url = models.URLField()
	developer = models.OneToOneField(User)
	price = models.FloatField()

	def __unicode__(self):
		return self.name
