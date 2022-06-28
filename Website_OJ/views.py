import imp
import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from  .models import Problem
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
    return render(request,'problem_statement.html',{'problem_data':problem_data,})
    
def Problem_list(request):
    problems = Problem.objects.all()
    serializer = ProblemSerializer(problems,many=True)
    return JsonResponse(serializer.data,safe=False)