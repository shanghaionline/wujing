from django.conf.urls import patterns, include, url
from chatroom import views

urlpatterns = patterns('',
                       url(r'^room/$', views.room_admin, name = 'room_admin'),
                       url(r'^room/(?P<name>[^/]+)', views.room, name = 'room'),
                       url(r'^push/', views.push, name = 'push'),
                       url(r'^poll/', views.poll, name = 'poll'),
                       url(r'^go-room/', views.go_room, name = 'go_room'),)
