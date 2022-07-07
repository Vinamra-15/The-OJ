from operator import sub
import docker
from codejudge.settings import BASE_DIR
from docker.models.containers import Container
import subprocess
import filecmp
import os


client = docker.from_env()
docker_img_python = 'python:3.8.11'
docker_img_gcc = 'gcc:11.2.0'


#takes submitted codefile, input test cases file and expected output test cases file,creates a docker container and judges for python submitted code
def dockerJudgePython(codeFileName,inputTCFileName,expectedOutputTCFileName,user):
    
    try:
        container:Container = client.containers.get(user) 
        if(container.status!='running'):
            container.start()
    except docker.errors.NotFound:
        container = client.containers.run(docker_img_python,detach=True,tty=True,name=user)
    

    #copy to code file to container
    subprocess.run(['docker', 'cp', codeFileName, container.id+':main.py'])
    
    #copy input test cases to container
    subprocess.run(['docker', 'cp', inputTCFileName, container.id+':input.txt'])

    verdict = 'WA'  #initialised verdict with wrong answer
    try:
        subprocess.run(['docker' ,'exec' , container.id,'bash','-c',"python main.py<input.txt>output.txt"],timeout=5)
        
        #copy output generated to local file
        returnedOutputTestCasesFileName = str(BASE_DIR)+'/'+'submissions/'+user+'returned_output.txt'
        subprocess.run(['docker', 'cp', container.id+':output.txt',returnedOutputTestCasesFileName])

        #remove extra lines from the end of returned output file
        with open(returnedOutputTestCasesFileName,'r') as f:
            text = f.read().rstrip()
        with open(returnedOutputTestCasesFileName, 'w') as f:
            f.write(text)

        #compare returned output with actual output
        
        if(filecmp.cmp(expectedOutputTCFileName,returnedOutputTestCasesFileName)):
            verdict = 'AC'
        
        os.remove(returnedOutputTestCasesFileName)


    except:
        verdict = 'WA'



    #close container

    subprocess.run(['docker','stop',container.id ])
    subprocess.run(['docker','rm',container.id ])


    return verdict


def dockerJudgeCPP(codeFileName,inputTCFileName,expectedOutputTCFileName,user):
    try:
        container:Container = client.containers.get(user) 
        if(container.status!='running'):
            container.start()
    except docker.errors.NotFound:
        container = client.containers.run(docker_img_gcc,detach=True,tty=True,name=user)

    #copy to code file to container
    subprocess.run(['docker', 'cp', codeFileName, container.id+':a.cpp'])
    
    #copy input test cases to container
    subprocess.run(['docker', 'cp', inputTCFileName, container.id+':input.txt'])

    verdict = 'WA'  #initialised verdict with wrong answer
    try:
        subprocess.run(['docker' ,'exec' , container.id,'bash','-c',"g++ a.cpp"],timeout=5)
        subprocess.run(['docker' ,'exec' , container.id,'bash','-c',"./a.out<input.txt>output.txt"],timeout=5)
        
        
        #copy output generated to local file
        returnedOutputTestCasesFileName = str(BASE_DIR)+'/'+'submissions/'+user+'returned_output.txt'
        subprocess.run(['docker', 'cp', container.id+':output.txt',returnedOutputTestCasesFileName])

        #remove extra lines from the end of returned output file
        with open(returnedOutputTestCasesFileName,'r') as f:
            text = f.read().rstrip()
        with open(returnedOutputTestCasesFileName, 'w') as f:
            f.write(text)

        #compare returned output with actual output
        
        if(filecmp.cmp(expectedOutputTCFileName,returnedOutputTestCasesFileName)):
            verdict = 'AC'
        
        os.remove(returnedOutputTestCasesFileName)


    except:
        verdict = 'WA'



    #close container

    subprocess.run(['docker','stop',container.id ])
    subprocess.run(['docker','rm',container.id ])
    


    return verdict

    

        
    


    



     



    
