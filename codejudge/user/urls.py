from django.contrib import admin
from django.urls import path,include
from user import views



urlpatterns = [
    path('login',views.loginUser,name="loginUser"),
    path('logout',views.logoutUser,name="logoutUser"),
    path('register',views.registerUser,name="registerUser"), 
]