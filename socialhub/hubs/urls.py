from django.conf.urls import patterns, url

from hubs import views

urlpatterns = patterns('',
    url(r'^$', views.hub_listing, name='hub_listing'),
    url(r'^(\d+)/$', views.hub_details, name='hub_details'),