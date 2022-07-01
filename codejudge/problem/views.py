from tkinter import S
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Problem

from .models import Problem
from leaderboard.models import Submission

# Create your views here.
@login_required(login_url='loginUser')

def problem(request,prob_id):
    problem = Problem.objects.get(id=prob_id)
    if request.method == 'POST':
        submittedCodeText = request.POST['submittedCodeText']
        submission = Submission(user=request.user,problem=problem,submitted_code = submittedCodeText)
        submission.save()
        print(submission)
        return redirect('leaderboard')

    problem = Problem.objects.get(id=prob_id)
    context = {
        'problem':problem
    }
    return render(request,'problem.html',context)
