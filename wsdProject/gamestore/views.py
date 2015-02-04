from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from gamestore.models import *
from hashlib import md5
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from gamestore.forms import UserData, UserForm, GameForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
import json
import time

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

#go back to developer homepage displaying the updated inventory 
def devhome(request):
	
	if request.user.is_authenticated():
		list_of_games = Games.objects.filter(developer=request.user)
		return render_to_response('gamestore/developer_homepage.html',context_instance=RequestContext(request, {'list_of_games':list_of_games}))
#load home page
def home(request):
	c={}
	c.update(csrf(request))
	return render_to_response('gamestore/home.html',c)

#start buying a game
def start_buy_view(request):
    c={}
    c.update(csrf(request))

    pid = "abcd"
    sid = "awesomegladiators"
    amount = 10
    secret_key = "3e200efab59d77550cb7893b1b944ded"
    checksum_str = "pid=%s&sid=%s&amount=%s&token=%s"%(pid, sid, amount, secret_key)

    m = md5(checksum_str.encode("ascii"))
    checksum = m.hexdigest()

    return render_to_response('gamestore/payment/start_buy.html', {'pid': pid, 'sid': sid, 'amount': amount, 'checksum': checksum})

#successful payment
def success_view(request):

    return render_to_response('gamestore/payment/success.html')

#canceled payment
def cancel_view(request):

    return render_to_response('gamestore/payment/cancel.html')

#error in payment
def error_view(request):

    return render_to_response('gamestore/payment/error.html')

#a game is added by a developer
def addgame(request):

	saved = False
	if request.method == 'POST':
		form = GameForm(data=request.POST)
		if form.is_valid():
			game = form.save(commit=False)
			game.developer = request.user
			game.save() 
			saved = True
		else:
			print(form.errors)
	else:
		form = GameForm()
			
	return render_to_response('gamestore/addgame.html',{'form': form, 'saved': saved},context_instance=RequestContext(request))

#called when a game is modified on the developer homepage
def editgame(request,id):

	game = Games.objects.get(pk=id)
	saved = False
	if request.method == 'POST':

		form = GameForm(data=request.POST)
		game.name = request.POST.get('name','')
		game.category = request.POST.get('category','')
		game.url = request.POST.get('url','')
		game.price = request.POST.get('price','')
		game.save()
		saved = True		
	else:
		form = GameForm(
			initial = { 'name' : game.name, 'category' : game.category, 'url' : game.url, 'price' : game.price }
		)
	
	return render_to_response('gamestore/editgame.html',{'game': game,'form': form, 'saved': saved},context_instance=RequestContext(request))

#delete a game on the developer homepage
def deletegame(request, id, template_name='gamestore/game_confirm_delete.html'):
	game = get_object_or_404(Games, pk=id)    
	if request.method=='POST':
		game.delete()
		return redirect('/devhome/')
	return render(request, template_name, {'object':game})

# load game.html with appropriate game iframe
def loadgame(request):

	player = request.user
	game = "testgame.html"
	return render_to_response('gamestore/game.html',{'player': player, 'game': game}, context_instance=RequestContext(request))

# display game statistics on the developer homepage
def gamestats(request):

	countlist = []
	datedict = {}
	if request.method=='POST' and request.is_ajax:
		id = request.POST.get('id',None)
		gameobj = Games.objects.filter(pk=id)
		d = { 'name' : gameobj[0].name, 'category': gameobj[0].category, 'url': gameobj[0].url, 'price': gameobj[0].price }
		# get queryset of Scores objects with the selected game ID
		scores = Scores.objects.filter(game=gameobj)
		# get list of distinct registration dates from "scores" queryset
		datelist = scores.values_list('registration_date',flat=True).distinct()
		for dateobj in datelist:
			scoredate = scores.filter(registration_date=dateobj)
			c = scoredate.count()
			countlist.append(c)

		n = len(countlist)
		for i in range(n):
			t = datelist[i].strftime('%d/%m/%Y')
			datedict[t] = countlist[i]
			print(t)
			print(datedict[t])

		json_stats = json.dumps(datedict)
		return HttpResponse(json_stats,content_type='application/json')


def savegamestate(request):

	if request.method=='POST' and request.is_ajax:
		
		data = json.loads(request.POST.get('jsondata', None))
		gamestate = data['gameState']

		# load player and game associated with this request, and use them to query the Scores object
		gameid = request.POST.get('gameid', None)
		playerid = request.POST.get('playerid', None)
		gameobj = Games.objects.get(pk=gameid)
		userobj = User.objects.get(pk=playerid)
		scoreobj = Scores.objects.filter(game=gameobj, player=userobj)

		scoreobj.update(last_score=gamestate["score"])

		# if the last score is higher than any of the 5 highest scores, replace that value to update the high scores list
		if gamestate["score"] > scoreobj[0].high_score_1:
			scoreobj.update(high_score_1=gamestate["score"])
		elif gamestate["score"] > scoreobj[0].high_score_2:
			scoreobj.update(high_score_2=gamestate["score"])
		elif gamestate["score"] > scoreobj[0].high_score_3:
			scoreobj.update(high_score_3=gamestate["score"])
		elif gamestate["score"] > scoreobj[0].high_score_4:
			scoreobj.update(high_score_4=gamestate["score"])
		elif gamestate["score"] > scoreobj[0].high_score_5:
			scoreobj.update(high_score_5=gamestate["score"])


		if scoreobj.update(gamestate=json.dumps(gamestate)) == 1:
			print('GAMESTATE SAVED SUCCESSFULLY!')


		json_state=json.dumps(gamestate)
		print(json_state)
		return HttpResponse(json_state, content_type='application/json')

# LOAD_REQUEST by the game is handled by this view
def loadgamestate(request):

	if request.method == 'POST' and request.is_ajax:
		data = json.loads(request.POST.get('jsondata', None))
		gameid = request.POST.get('gameid', None)
		playerid = request.POST.get('playerid', None)
		gameobj = Games.objects.get(pk=gameid)
		userobj = User.objects.get(pk=playerid)
		scoreobj = Scores.objects.filter(game=gameobj, player=userobj)

		if scoreobj[0].gamestate is None:
			data["messageType"] = "MESSAGE"
			data["message"] = "No gamestate to be loaded"

		else:
			data["messageType"] = "LOAD"
			data["gameState"] = scoreobj[0].gamestate
			print(scoreobj[0].gamestate)	

		json_state=json.dumps(data)
		return HttpResponse(json_state, content_type='application/json')
















	

