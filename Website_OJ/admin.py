from django.contrib import admin

# Register your models here.
from .models import Member, Problem, Submission, Test_cases, File

admin.site.register(Member)
admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(Test_cases)
admin.site.register(File)
