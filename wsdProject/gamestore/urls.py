from django.conf.urls import patterns, include, url
from django.contrib import admin
import gamestore.views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'wsdProject.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^signup/$', gamestore.views.signup, name=' register_url'),
	url(r'^newlogin/', gamestore.views.newlogin, name= ' new_login'),
	url(r'^home/', gamestore.views.newlogin, name= ' home'),
)
