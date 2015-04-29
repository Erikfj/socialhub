from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = ('',
	url(r'^$', include('theme.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Examples:
    # url(r'^$', 'socialhub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
