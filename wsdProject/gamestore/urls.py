from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import gamestore.views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'wsdProject.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^signup/$', gamestore.views.signup, name=' register_url'),
	url(r'^newlogin/', gamestore.views.newlogin, name= ' new_login'),
	url(r'^home/', gamestore.views.newlogin, name= ' home'),
	url(r'^add/', gamestore.views.addgame, name= ' add'),
	url(r'^login/', gamestore.views.devhome, name= ' dev_home'),
	url(r'^delete/', gamestore.views.deletegame, name= ' deletegame'),
	url(r'^game/', gamestore.views.loadgame, name= ' load_game'),
	url(r'^testgame/', TemplateView.as_view(template_name="gamestore/testgame.html"),name=' testgame'),
)
