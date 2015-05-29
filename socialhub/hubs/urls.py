from django.conf.urls import patterns, url

from hubs import views

urlpatterns = patterns('',
    url(r'^$', views.hub_listing, name='hub_listing'),
    url(r'^(\d+)/$', views.hub_details, name='hub_details'),
    url(r'^(\d+)/add_points/(\d+)$', views.hub_topic_add_points, 
    	name='hub_topic_add_points'),
)