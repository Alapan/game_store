from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import gamestore.views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'wsdProject.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^payment/start_buy/', 'gamestore.views.start_buy_view'),
	url(r'^payment/success/', 'gamestore.views.success_view'),
	url(r'^payment/cancel/', 'gamestore.views.cancel_view'),
	url(r'^payment/error/', 'gamestore.views.error_view'),

	url(r'^signup/$', gamestore.views.signup, name=' register_url'),
	url(r'^game/', gamestore.views.playerhomepage, name= 'player_homepage '),
	url(r'^start_buy/', gamestore.views.startbuy, name= 'startbuy '),
	url(r'^newlogin/', gamestore.views.newlogin, name= ' new_login'),
	url(r'^home/', gamestore.views.newlogin, name= ' home'),
	url(r'^add/', gamestore.views.addgame, name= ' add'),
	url(r'^login/', gamestore.views.devhome, name= ' dev_home'),
	url(r'^delete/', gamestore.views.deletegame, name= ' deletegame'),
	url(r'^loadgame/', gamestore.views.loadgame, name= ' load_game'),
	url(r'^testgame/', TemplateView.as_view(template_name="gamestore/testgame.html"),name=' testgame'),
)
