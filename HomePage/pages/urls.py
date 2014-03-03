from django.conf.urls import patterns, url
from HomePage.pages import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'essays/(?P<essay_id>\d+)/$', views.essay, name='essay'),
    url(r'resume/$', views.resume, name='resume')
)

urlpatterns += staticfiles_urlpatterns()
