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
from gamestore.forms import UserData, UserForm

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
			return render_to_response('gamestore/developer_homepage.html',c,context_instance=RequestContext(request))
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

def home(request):
	c={}
	c.update(csrf(request))
	return render_to_response('gamestore/home.html',c)

def addgame(request):

	c={}
	c.update(csrf(request))
	saved = False
	if request.method == 'POST':
		name = request.POST['name']
		#print(name)
		category = request.POST['category']
		#print(category)
		url = request.POST['url']
		#print(url)
		developer = request.POST['developer']
		#print(developer)
		price = request.POST['price']
		#print(price)
		game = Games(name,category,url,developer,price)
		game.save()
		saved = True
		return render_to_response('gamestore/developer_homepage.html',{'saved':saved},context_instance=RequestContext(request))
