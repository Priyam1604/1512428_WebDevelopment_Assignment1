from django.urls import path,include
from django.contrib.auth import views as auth_views

from django.shortcuts import render

# Create your views here.


urlpatterns = {
    path('login/',auth_views.LoginView.as_View()),
}