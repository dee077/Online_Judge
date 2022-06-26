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
    return render(request,'home.html',{'json_data':json_data})

def problem_statement(request):
    json_data = requests.get('http://127.0.0.1:8000/api').json()
    print(json_data)
    return render(request,'problem_statement.html',{'json_data':json_data})
    
def Problem_list(request):
    problems = Problem.objects.all()
    serializer = ProblemSerializer(problems,many=True)
    return JsonResponse(serializer.data,safe=False)