from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'HomePage.pages.views.home', name='home'),
    url(r'^pages', include('HomePage.pages.urls')),
)
