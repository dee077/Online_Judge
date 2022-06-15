
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
