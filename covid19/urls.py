from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePage,name="home"),
    path("login/",loginPage,name="login"),
    path('logout/', logoutUser, name="logout")

]
