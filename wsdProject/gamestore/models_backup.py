from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, unique=True)
    usertype = models.BooleanField(default=1)                   # 1 equals Player, 0 equals Developer

    def __unicode__(self):
        return self.user_name


class Games(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField()
    developer = models.OneToOneField(Users)
    price = models.FloatField()

    def __unicode__(self):
        return self.name
