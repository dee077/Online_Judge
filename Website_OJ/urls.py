from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('problem/<int:p_id>',views.problem_statement,name='problem'),
]