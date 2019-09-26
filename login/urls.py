from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$',  LogoutView.as_view(template_name='logged_out.html'), name='logout'),
]
