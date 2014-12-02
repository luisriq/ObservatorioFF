from django.conf.urls import patterns, url

from twitter import views

urlpatterns = patterns('',
    url(r'^(\w*)$', views.home, name='home'),
)