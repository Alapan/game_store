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
		# create Usertype object with submitted information
		user_form = UserForm(data=request.POST)
		print(user_form)
		# if object is valid, save to database
		if user_form.is_valid():
			#user = user_form.save()
			#hash the password and save
			#user.set_password(user.password)
			#user.save()
			#registered = True
			profile = user_form.save(commit=False)
			profile.user.username = user_form['username']
			profile.user.first_name = user_form['firstname']
			profile.user.last_name = user_form['lastname']
			profile.user.email = user_form['email']
			profile.user.first_name = user_form['email']
			profile.usertype = user_form['usertype']

			profile.save()	
		else:
			#print(data)
			print(user_form.errors)
	# not HTTP POST, so the template form is rendered using Usertypes instances. The form will be blank.
	else:
		user_form = UserForm()

	# render the template depending on the context
	return render_to_response('gamestore/registration.html',{'user_form': user_form, 'registered': registered},context_instance=RequestContext(request))
		
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
