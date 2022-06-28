from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginUser,name="loginUser"),
    path('logout',views.logoutUser,name="logoutUser"),
    path('register',views.registerUser,name="registerUser"),
    
    
]