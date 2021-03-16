from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePage,name="home"),
    path("login/",loginUser,name="login"),
    path("symptom_analysis/",symptomAnalysis,name="symptom"),
    path("logout/",logoutUser,name="logout")

]
