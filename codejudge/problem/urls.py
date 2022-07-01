from django.contrib import admin
from django.urls import path,include
from  problem import views

urlpatterns = [
    path('<int:prob_id>',views.problem,name="problem"),
       
]