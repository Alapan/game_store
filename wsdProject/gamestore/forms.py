from django.contrib.auth.models import User
from django import forms
from gamestore.models import Usertypes, Games

class UserData(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('first_name','last_name','username', 'email', 'password')

class UserForm(forms.ModelForm):
		CHOICES = (
				('player','Player',),('developer','Developer')
		)

		usertype = forms.ChoiceField(widget=forms.Select(),choices=CHOICES, required=True, label='User type ')
		class Meta:
				model = Usertypes
				fields = ('usertype',)

class GameForm(forms.ModelForm):

	CHOICES = (
				('Adventure','Adventure',),('Football','Football'),('Puzzle', 'Puzzle'),('Racing', 'Racing'), ('Sports','Sports')
		)

	category = forms.ChoiceField(widget=forms.Select(),choices=CHOICES, required=True, label='Category')
	class Meta:
		model = Games
		fields = ('name','category','url','price')
