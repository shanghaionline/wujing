from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wujing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace = 'accounts')),
    url(r'^chatroom/', include('chatroom.urls', namespace = 'chatroom')),
    url(r'^board/', include('msgboard.urls', namespace = 'msgboard')),
)
