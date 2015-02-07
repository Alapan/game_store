from django.conf.urls import patterns, include, url
from django.contrib import admin
import gamestore.views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'wsdProject.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

    url(r'^payment/start_buy/(\d{1,4})/', 'gamestore.views.start_buy_view'),
    url(r'^payment/success/', 'gamestore.views.success_view'),
    url(r'^payment/cancel/', 'gamestore.views.cancel_view'),
    url(r'^payment/error/', 'gamestore.views.error_view'),
    url(r'^game_info/(\d{1,4})/', 'gamestore.views.game_info_view'),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$','gamestore.views.home'),
	url(r'^login/','gamestore.views.login_view'),
	url(r'^logout/','gamestore.views.logout_view'),
	url(r'^registration/','gamestore.views.registration'),
	url(r'^addgame/','gamestore.views.addgame'),
	url(r'^devhome/','gamestore.views.devhome'),
	url(r'^gamestats/','gamestore.views.gamestats'),
	url(r'^savegamestate/','gamestore.views.savegamestate'),
	url(r'^loadgamestate/','gamestore.views.loadgamestate'),
	url(r'^editgame/(?P<id>\d+)/','gamestore.views.editgame'),
	url(r'^delete/(?P<id>\d+)/','gamestore.views.deletegame'),
	url(r'^gamestore/', include('gamestore.urls', namespace="gamestore")),
)
