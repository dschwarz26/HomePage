from django.conf.urls import patterns, url
from HomePage.pages import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'resume/$', views.resume, name='resume')
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
