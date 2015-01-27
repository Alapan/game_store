from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from gamestore.models import *
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from gamestore.forms import UserData, UserForm, GameForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,redirect

# Create your views here.

def signup(request):
	# User clicks on 'Sign up' link on homepage. This returns the registration page
	c = {}
	c.update(csrf(request))
	return render_to_response('gamestore/registration.html',c,context_instance=RequestContext(request))

def newlogin(request):
	# After successfully registering, the user logins in from the home page.
	c = {}
	c.update(csrf(request))
	return render_to_response('gamestore/home.html',c,context_instance=RequestContext(request))

# register a new user as player or developer
def registration(request):
	c = {}
	c.update(csrf(request))
	# a boolean value for telling the template if the registration was successful or not
	registered = False
	# if it is HTTP POST, form data have to be processed
	if request.method == 'POST':
		user_data = UserData(data=request.POST)
		user_form = UserForm(data=request.POST)
		# if object is valid, save to database
		if user_data.is_valid() and user_form.is_valid():
			user = user_data.save()
			#hash the password and save
			user.set_password(user.password)
			user.save()
			#registered = True
			profile = user_form.save(commit=False)
			profile.user = user
			profile.save()	
			registered = True
			sendmail(user)
			#print(user.first_name,user.email)
		else:
			#print(data)
			print(user_data.errors, user_form.errors)
	# not HTTP POST, so the template form is rendered using Usertypes instances. The form will be blank.
	else:
		user_data = UserData()
		user_form = UserForm()

	# render the template depending on the context
	return render_to_response('gamestore/registration.html',{'user_data': user_data, 'user_form': user_form, 'registered': registered},context_instance=RequestContext(request))

# send email to a new user after successful registration
def sendmail(user):
	subject = 'Registration confirmation mail'
	message = 'Dear ' + user.first_name + ''', 

Thank you for registering on our website!

Best regards,
The Gladiators team'''
	from_email = 'no-reply@gladiator.com'
	recipient_list = []
	recipient_list.append(user.email)
	send_mail(subject, message, from_email, recipient_list, fail_silently=False)
		
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
		if usertype == 'player' and user.usertypes.usertype == usertype:
			return render_to_response('gamestore/player_homepage.html',c,context_instance=RequestContext(request))
		#if user is a developer, load developer homepage
		elif usertype == 'developer' and user.usertypes.usertype == usertype:
			list_of_games = Games.objects.filter(developer=user)
			return render_to_response('gamestore/developer_homepage.html',context_instance=RequestContext(request, {'list_of_games':list_of_games}))
		#user exists but incorrect type entered
		else:	
			return render_to_response('gamestore/usertype_error.html',c)

	else:
		#Redirect to login page, as login is incorrect
		return render_to_response('gamestore/home.html',c)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):

	#c={}
	#c.update(csrf(request))
	logout(request)
	#request.session.flush()
	#request.user = AnonymousUser
	#Redirect to logout page
	return render_to_response('gamestore/logout.html')

def devhome(request):
	
	if request.user.is_authenticated():
		list_of_games = Games.objects.filter(developer=request.user)
		return render_to_response('gamestore/developer_homepage.html',context_instance=RequestContext(request, {'list_of_games':list_of_games}))

def home(request):
	c={}
	c.update(csrf(request))
	return render_to_response('gamestore/home.html',c)

def addgame(request):

	c={}
	c.update(csrf(request))
	saved = False
	if request.method == 'POST':
		form = GameForm(data=request.POST)
		if form.is_valid():
			game = form.save(commit=False)
			game.developer = request.user
			print(game.developer)
			game.save() 
			saved = True
		else:
			print(form.errors)
	else:
		form = GameForm()
			
	return render_to_response('gamestore/addgame.html',{'form': form, 'saved': saved},context_instance=RequestContext(request))

def deletegame(request, id, template_name='gamestore/game_confirm_delete.html'):
	game = get_object_or_404(Games, pk=id)    
	if request.method=='POST':
		game.delete()
		return redirect('/devhome/')
	return render(request, template_name, {'object':game})
