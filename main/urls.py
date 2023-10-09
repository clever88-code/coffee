from argparse import ArgumentDefaultsHelpFormatter
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    #path('', views.add_record, name='add_record')
    

  



]