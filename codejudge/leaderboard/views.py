from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def leaderboard(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'leaderboard.html')



