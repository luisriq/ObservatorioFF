from django.conf.urls import patterns, url


from twitter import views
from twitter import jsonController

urlpatterns = patterns('',
	url(r'^json/(\w*)$', jsonController.home,name='datos'),
	url(r'^index/(\w*)$', jsonController.tweets, name='casa'),
	url(r'^(\w*)$', views.home, name='home'),
	
)
