from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api',views.Problem_list,name='api'),
    path('problem/<int:p_id>',views.problem_statement,name='problem'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)