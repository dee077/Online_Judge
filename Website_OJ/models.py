
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
    problem_id = models.ForeignKey(Problem,on_delete=models.DO_NOTHING)
    input_case = models.CharField(max_length=200)
    output_case = models.CharField(max_length=200)

class Submission(models.Model):
    problem_id = models.ForeignKey(Problem,on_delete=models.DO_NOTHING)
    submission_time = models.TimeField(null=True)
    verdict = models.CharField(max_length=200)

