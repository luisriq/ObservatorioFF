from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cadenas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('twitter.urls'), name='home'),
    
)