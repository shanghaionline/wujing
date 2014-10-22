from django.conf.urls import patterns, include, url
from accounts import views
urlpatterns = patterns('',
  url(r'^register/', views.SignUpView.as_view(), name = 'register'),
  url(r'^login/', 'django.contrib.auth.views.login', {'template_name':'accounts/login.html'}, name = 'login'),
  url(r'^logout/', 'django.contrib.auth.views.logout', {'template_name':'accounts/logged_out.html'}, name = 'logout'),
  url(r'^profile/', views.profile, name = 'profile'),
)
