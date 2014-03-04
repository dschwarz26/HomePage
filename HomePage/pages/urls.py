from django.conf.urls import patterns, url
from HomePage.pages import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'essays/(?P<essay_name>\w+)/$', views.essay, name='essay'),
    url(r'biopics/(?P<biopic_name>\w+)/$', views.biopic, name='biopic'),
    url(r'personal/(?P<personal_name>\w+)/$', views.personal, name='personal'),
    url(r'resume/$', views.resume, name='resume')
)

urlpatterns += staticfiles_urlpatterns()
