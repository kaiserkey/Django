from django.urls import path
from . import views
from .models import Project, Task

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('datos/<str:username>', views.datos),
    path('project/', views.project),
    path('task/', views.task),
    
]
