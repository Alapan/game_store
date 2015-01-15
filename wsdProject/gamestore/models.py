from django.contrib.auth.models import User
from django.db import models


class Usertypes(models.Model):
    user = models.OneToOneField(User)
    usertype = models.BooleanField(default=True)                   # True equals Player, False equals Developer

    def __unicode__(self):
        return self.user_name


#class Games(models.Model):
#    name = models.CharField(max_length=100, unique=True)
#    url = models.URLField()
#    developer = models.OneToOneField(Users)
#    price = models.FloatField()

#    def __unicode__(self):
#        return self.name
