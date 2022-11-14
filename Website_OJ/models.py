
from ast import mod
from xmlrpc.client import DateTime
from django.db import models


# Create your models here.
class Member(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phoneno = models.IntegerField()
    age = models.IntegerField()
    college = models.CharField(max_length=200)
    passingyear = models.IntegerField()
    address = models.CharField(max_length=200)
    passwd = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname

class Problem(models.Model):
    problem_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    statement = models.CharField(max_length=2000)
    difficulty = models.CharField(max_length=200)
    solved_status = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Test_cases(models.Model):
    p_id = models.IntegerField(default=1,primary_key=True)
    input_file = models.FileField(null=True)
    correct_output = models.FileField(null=True)


class Submission(models.Model):
    file_name = models.FileField(null=True)
    
    def __str__(self):
        return self.file
