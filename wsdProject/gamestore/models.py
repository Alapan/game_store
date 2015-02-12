from django.contrib.auth.models import User
from django.db import models

class Usertypes(models.Model):
	user = models.OneToOneField(User)
	developer = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user_name

class Games(models.Model):
	name = models.CharField(max_length=100,unique=True)
	category = models.CharField(max_length=100)
	url = models.URLField()
	developer = models.ForeignKey(User)
	description = models.CharField(max_length=250, default='description goes here')
	price = models.FloatField()

	def __unicode__(self):
		return self.name

class Scores(models.Model):
	game = models.ForeignKey(Games)
	player = models.ForeignKey(User)
	registration_date = models.DateField(auto_now=False, auto_now_add=False)
	gamestate = models.TextField(blank=True, null=True)
	high_score_1 = models.PositiveIntegerField(default=0)
	high_score_2 = models.PositiveIntegerField(default=0)
	high_score_3 = models.PositiveIntegerField(default=0)
	high_score_4 = models.PositiveIntegerField(default=0)
	high_score_5 = models.PositiveIntegerField(default=0)
	last_score = models.PositiveIntegerField(default=0)


	def __unicode__(self):
		return self.game
