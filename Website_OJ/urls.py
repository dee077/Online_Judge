from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('problem/<int:p_id>',views.problem_statement,name='problem'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)