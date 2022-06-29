from django.contrib import admin
from django.urls import path,include
from leaderboard import views

urlpatterns = [
    path('leaderboard',views.leaderboard,name="leaderboard"),  
]