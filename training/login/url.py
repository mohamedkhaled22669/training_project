from django.contrib import admin 
from django.urls import path 

from login import views

from django.views.generic import TemplateView

urlpatterns = [
    path("login/", TemplateView.as_view(template_name = 'login/login.html'),name='login'),
    path("login/success/",views.success_login),
    
    
    
    path("reg/", TemplateView.as_view(template_name = 'login/register.html'),name = 'register'),
    path("reg/success/",views.success_register),
    
    path("logout/",views.logout),
    
    
]