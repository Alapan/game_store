from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import gamestore.views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'wsdProject.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

    url(r'^payment/start_buy/(\d{1,4})/', gamestore.views.start_buy_view, name=' start_buy'),
    url(r'^payment/success/', gamestore.views.success_view, name=' success'),
    url(r'^payment/cancel/', gamestore.views.cancel_view, name=' cancel'),
    url(r'^payment/error/', gamestore.views.error_view, name=' error'),
    url(r'^game_info/(\d{1,4})/', gamestore.views.game_info_view, name=' game_info'),
    url(r'^search/', gamestore.views.search_view, name=' search'),
    url(r'^category/all/', gamestore.views.all_view, name=' all'),
    url(r'^category/(\w+)/', gamestore.views.category_view, name=' category'),
    url(r'^playerhome/', gamestore.views.playerhome, name=' player_homepage'),
    url(r'^verify/(\w+)/', gamestore.views.verify, name=' verify'),
	#url(r'^facebook/', include('django_facebook.urls')),
	url(r'^help/', gamestore.views.help, name= 'help'),
	url(r'^about/',gamestore.views.about, name='about'),


	url(r'^signup/$', gamestore.views.signup, name=' register_url'),
	#url(r'^game/', gamestore.views.playerhomepage, name= 'player_homepage '),
	#url(r'^start_buy/', gamestore.views.startbuy, name= 'startbuy '),
	url(r'^home/', gamestore.views.home, name= ' home'),
    url(r'^$', gamestore.views.home, name=' home'),
	url(r'^add/', gamestore.views.addgame, name= ' add'),
	url(r'^login/', gamestore.views.devhome, name= ' dev_home'),
	url(r'^delete/', gamestore.views.deletegame, name= ' deletegame'),
	url(r'^loadgame/', gamestore.views.loadgame, name= ' load_game'),
	url(r'^testgame/', TemplateView.as_view(template_name="gamestore/testgame.html"),name=' testgame'),
    url(r'^.*/$',gamestore.views.notfound, name='notfound'),
)
