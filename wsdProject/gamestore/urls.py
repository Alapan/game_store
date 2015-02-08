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

	url(r'^signup/$', gamestore.views.signup, name=' register_url'),
	url(r'^newlogin/', gamestore.views.newlogin, name= ' new_login'),
	url(r'^home/', gamestore.views.newlogin, name= ' home'),
	url(r'^add/', gamestore.views.addgame, name= ' add'),
	url(r'^login/', gamestore.views.devhome, name= ' dev_home'),
	url(r'^delete/', gamestore.views.deletegame, name= ' deletegame'),
	url(r'^game/', gamestore.views.loadgame, name= ' load_game'),
	url(r'^testgame/', TemplateView.as_view(template_name="gamestore/testgame.html"),name=' testgame'),
)
