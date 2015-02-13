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
				(False,'Remain as player',),(True,'Upgrade to developer')
		)

		developer = forms.ChoiceField(widget=forms.Select(),choices=CHOICES, required=True, label='Do you want to remain as player or upgrade to developer? ')
		class Meta:
				model = Usertypes
				fields = ('developer',)

class GameForm(forms.ModelForm):

	CHOICES = (
				('Adventure','Adventure',),('Football','Football'),('Puzzle', 'Puzzle'),('Racing', 'Racing'), ('Sports','Sports')
		)

	category = forms.ChoiceField(widget=forms.Select(),choices=CHOICES, required=True, label='Category')
	class Meta:
		model = Games
		fields = ('name','category','description','url','price')
