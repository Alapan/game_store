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
	username = request.POST.get('username',False)
	password = request.POST.get('password',False)
	usertype = request.POST.get('usertype',False)
	user = authenticate(username=username,password=password)

	#password was correctly matched against the username, thus valid user object is returned
	if user is not None:
		login(request,user)
		#if user is a player, load player homepage
		if usertype == True and user.usertypes.usertype == usertype:
			return render_to_response('gamestore/player_homepage.html',c,context_instance=RequestContext(request))
		#if user is a developer, load developer homepage
		elif usertype == False and user.usertypes.usertype == usertype:
			return render_to_response('gamestore/developer_homepage.html',c,context_instance=RequestContext(request))
		#user exists but incorrect type entered
		else:	
			print(usertype)
			return render_to_response('gamestore/usertype_error.html',c)

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
