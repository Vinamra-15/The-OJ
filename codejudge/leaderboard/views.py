import imp
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Submission



# Create your views here.
def leaderboard(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    submissions = Submission.objects.all().order_by('-submission_time')
    context = {
        'submissions':submissions
    }
    return render(request,'leaderboard.html',context)



