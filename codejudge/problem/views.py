import subprocess
import os
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Problem
from codejudge.settings import BASE_DIR
import filecmp
from leaderboard.models import Submission
from datetime import datetime
from .judge import dockerJudgePython
from .judge import dockerJudgeCPP


# Create your views here.
@login_required(login_url='loginUser')

def problem(request,prob_id):
    problem = Problem.objects.get(id=prob_id)
    if request.method == 'POST':

        submittedCodeText = request.POST['submittedCodeText']
        submittedCodeLanguage = request.POST['language']

        #judging python code
        if(submittedCodeLanguage=='Python'):
            filename = str(BASE_DIR)+'/'+'submissions/'+request.user.username+'new_file.py'
            inputTestCasesFileName = problem.inputTestCases
            outputTestCasesFileName = problem.outputTestCases
            #returnedOutputTestCasesFileName = str(BASE_DIR)+'/'+'submissions'+'/returned_output.txt'

            file = open(filename, 'w')
            file.write(submittedCodeText)
            file.close()

            verdict = dockerJudgePython(filename,inputTestCasesFileName,outputTestCasesFileName,request.user.username+'python')

            if(verdict=='AC'):
                submission = Submission(submitted_code = submittedCodeText,compiler='python',user=request.user,problem=problem,verdict='AC',submission_time=datetime.now())
                submission.save()
            else:
                submission = Submission(submitted_code = submittedCodeText,compiler='python',user=request.user,problem=problem,verdict='WA',submission_time=datetime.now())
                submission.save()
            
            os.remove(filename) 


        #judging c++ code
        else:
            filename = str(BASE_DIR)+'/'+'submissions/'+request.user.username+'new_file.cpp'
            inputTestCasesFileName = str(problem.inputTestCases)
            outputTestCasesFileName = problem.outputTestCases
            

            file = open(filename, 'w')
            file.write(submittedCodeText)
            file.close()
        

            verdict = dockerJudgeCPP(filename,inputTestCasesFileName,outputTestCasesFileName,request.user.username+'cpp')

            if(verdict=='AC'):
                submission = Submission(submitted_code = submittedCodeText,compiler='c++',user=request.user,problem=problem,verdict='AC',submission_time=datetime.now())
                submission.save()
            else:
                submission = Submission(submitted_code = submittedCodeText,compiler='c++',user=request.user,problem=problem,verdict='WA',submission_time=datetime.now())
                submission.save()
            
            os.remove(filename)

    
        

        return redirect('leaderboard')

    problem = Problem.objects.get(id=prob_id)
    context = {
        'problem':problem
    }
    return render(request,'problem.html',context)
