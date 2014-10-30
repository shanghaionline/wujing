from django.conf.urls import patterns, include, url
from msgboard import views

urlpatterns = patterns(
    '',
    url(r'^list/(?P<page>\d+)$', views.list, name = 'list'),
    url(r'^agree/$', views.agree, name = 'agree'),
    url(r'^post/$', views.post, name = 'post')
)
