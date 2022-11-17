import imp,subprocess
import json
from xml.dom.minidom import Document
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from  .models import Problem,Submission, Test_cases
from .serializers import ProblemSerializer
from rest_framework.renderers import JSONRenderer
import requests ,subprocess ,filecmp

def home(request):
    json_data = Problem.objects.all()
    print(json_data)
    return render(request,'home.html',{'json_data':json_data})

def problem_statement(request,p_id):
    problem_data=Problem.objects.get(problem_id=p_id)
    verdict="0"
    if request.method == "POST":
        submitted_file=request.FILES[ "file"]
        document=Submission.objects.create(file_name=submitted_file)
        document.save()
        verdict="NULL"
        io_file = Test_cases.objects.get(p_id=p_id)
        input_file=io_file.input_file
        correct_op=io_file.correct_output
        current_submitted_file=Submission.objects.get(id=document.id)
        current_submitted_file=current_submitted_file.file_name

        subprocess.run(["Docker","start","code_compiler"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        # docker cp input output and cpp
        subprocess.run(["docker","cp","code_files/"+input_file.name,"code_compiler:/usr/src/input.txt"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        subprocess.run(["docker","cp","code_files/output.txt","code_compiler:/usr/src/"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        subprocess.run(["docker","cp","code_files/"+current_submitted_file.name,"code_compiler:/usr/src/test.cpp"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
        # docker execut and copy back
        subprocess.run(["docker","exec","code_compiler","python3","compiler.py"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        subprocess.run(["docker","cp","code_compiler:/usr/src/output.txt","code_files/output.txt"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
        # docker stop
        subprocess.run(["Docker","stop","code_compiler"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)

        # output file compare
        f1=open("C:/Users/deepa/OneDrive/Documents/Django/Online_Judge/code_files/"+correct_op.name,'r')
        f2=open("C:/Users/deepa/OneDrive/Documents/Django/Online_Judge/code_files/output.txt",'r')  
        i = 0
        x=0
        for line1 in f1:
            i += 1 
            for line2 in f2:
                if line1 != line2:
                    x=1  
                    break
        f1.close()                                       
        f2.close()
        if x==0:
            verdict="True"
        else:
            verdict="False"
    return render(request,'problem_statement.html',{'problem_data':problem_data,'verdict':verdict})
    
def Problem_list(request):
    problems = Problem.objects.all()
    serializer = ProblemSerializer(problems,many=True)
    return JsonResponse(serializer.data,safe=False)

