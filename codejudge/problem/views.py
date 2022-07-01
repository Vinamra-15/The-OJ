from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Problem

# Create your views here.
@login_required(login_url='loginUser')

def problem(request,prob_id):
    problem = Problem.objects.get(id=prob_id)
    context = {
        'problem':problem
    }
    return render(request,'problem.html',context)
