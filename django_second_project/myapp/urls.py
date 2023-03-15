from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('datos/', views.datos, name='datos'),
    path('project/', views.project, name='project'),
    path('task/', views.task, name='task'),
    path('new_task/', views.newTask, name='create_task'),
    path('new_project/', views.newProject, name='create_project')
]
