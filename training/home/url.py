from home.views import add_node_success
from django.contrib import admin 
from django.urls import path 

from home import views

from django.views.generic import TemplateView

urlpatterns = [
    path("",views.home,name='home'),
    
    path("add/",views.add_node,name='addnode'),
    path("add/success/",views.add_node_success),
    
    path("delete/",views.delete_node),
    
    path("update/",views.update_node),
    
    path("send/",views.send_node),
    path("send/success/",views.send_node_success),
    

    
    # path("testhome/",views.testhome),
]