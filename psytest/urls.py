from django.conf.urls import patterns, include, url
from psytest import views
urlpatterns = patterns(
    '',
    url(r'^show/$', views.show),
)

