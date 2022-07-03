import subprocess
import os
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Problem
from codejudge.settings import BASE_DIR
import filecmp
from leaderboard.models import Submission
from datetime import datetime
from django.contrib import messages

# Create your views here.
@login_required(login_url='loginUser')

def problem(request,prob_id):
    problem = Problem.objects.get(id=prob_id)
    if request.method == 'POST':


        submittedCodeText = request.POST['submittedCodeText']
        
        

        

        #judging python code
        filename = str(BASE_DIR)+'/'+'submissions'+'/new_file.py'
        inputTestCasesFileName = problem.inputTestCases
        outputTestCasesFileName = problem.outputTestCases
        returnedOutputTestCasesFileName = str(BASE_DIR)+'/'+'submissions'+'/returned_output.txt'

        file = open(filename, 'w')
        file.write(submittedCodeText)
        file.close()
       

        inputTC = open(inputTestCasesFileName,'r')
 
        outputTC = open(outputTestCasesFileName,'r')

        returnedOutputTC = open(returnedOutputTestCasesFileName,'w')
        
        p = subprocess.run(['python',filename],stdin=inputTC,stdout=returnedOutputTC)
        inputTC.close()
        outputTC.close()
        
        #remove extra lines from the end of returned output file
        with open(returnedOutputTestCasesFileName,'r') as f:
            text = f.read().rstrip()


        with open(returnedOutputTestCasesFileName, 'w') as f:
            f.write(text)

        returnedOutputTC.close()

        # saving submissions to db if accepted
        if(filecmp.cmp(outputTestCasesFileName,returnedOutputTestCasesFileName)):
            submission = Submission(submitted_code = submittedCodeText,user=request.user,problem=problem,verdict='AC',submission_time=datetime.now())
            print(submission.submission_time)
            submission.save()
        else:
            submission = Submission(submitted_code = submittedCodeText,user=request.user,problem=problem,verdict='WA',submission_time=datetime.now())
            submission.save()



        #remove extra generated files
        os.remove(returnedOutputTestCasesFileName)
        os.remove(filename)
    
        

        return redirect('leaderboard')

    problem = Problem.objects.get(id=prob_id)
    context = {
        'problem':problem
    }
    return render(request,'problem.html',context)
