from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
