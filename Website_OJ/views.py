import imp
import json
from xml.dom.minidom import Document
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from  .models import Problem,File
from .serializers import ProblemSerializer
from rest_framework.renderers import JSONRenderer
import requests

def home(request):
    json_data = requests.get('http://127.0.0.1:8000/api').json()
    # print(json_data[0]['problem_id'])
    return render(request,'home.html',{'json_data':json_data})

def problem_statement(request,p_id):
    json_data = requests.get('http://127.0.0.1:8000/api').json()
    problem_data=json_data[p_id-1]
    if request.method == "POST":
        file1=request.FILES[ "file"]
        # code_data=request.POST["code_data"]
        document1=File.objects.create(file=file1)
        document1.save()
    return render(request,'problem_statement.html',{'problem_data':problem_data,})
    
def Problem_list(request):
    problems = Problem.objects.all()
    serializer = ProblemSerializer(problems,many=True)
    return JsonResponse(serializer.data,safe=False)