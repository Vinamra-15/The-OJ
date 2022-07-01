from genericpath import exists
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from problem.models import Problem
from leaderboard.models import Submission



# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    problems = Problem.objects.all()
    # submitted_by_user = Submission.objects.filter(user=request.user.id)
    contextData = list(problems.values())
   
    
    contextDataIndex = 0
    for problem in problems:
        submitted_by_user = Submission.objects.filter(user=request.user.id,problem=problem)
        data = contextData[contextDataIndex]
        data.__setitem__('verdict','-')
        contextData[contextDataIndex] = data
        
        
        


        for sub in submitted_by_user:
            if sub.verdict=='AC':
                contextData[contextDataIndex]['verdict'] = 'ACCEPTED'
                break
            else:
                contextData[contextDataIndex]['verdict'] = 'REJECTED'
        contextDataIndex = contextDataIndex + 1


        
    


    # contextData = problems.values()
    # for problem in contextData:
    #     problem['verdict'] = 'Not Attempted'
    #     for submission in submitted_by_user:
    #         if submission

            
    
    context = {
        'problems': contextData,
        
    }
    
    return render(request,'index.html',context)



