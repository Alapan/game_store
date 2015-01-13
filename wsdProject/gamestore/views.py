from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from gamestore.models import *

# Create your views here.

def login_view(request):

	c={}
	c.update(csrf(request))        
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username,password=password)

	#password was correctly matched against the username
	if user is not None:
		#user account is active
		if user.is_active:
			login(request,user)
			#Redirect to user's homepage
			return render_to_response('gamestore/user_homepage.html',c,context_instance=RequestContext(request))
		else:
			#Return a 'disabled account' error message
			return render_to_response('gamestore/account_disabled.html',c)

	else:
		#Redirect to login page, as login is incorrect
		return render_to_response('gamestore/home.html',c)


def logout_view(request):

	#c={}
	#c.update(csrf(request))
	logout(request)
	#Redirect to logout page
	return render_to_response('gamestore/logout.html')

def home(request):
	c={}
	c.update(csrf(request))
	return render_to_response('gamestore/home.html',c)
