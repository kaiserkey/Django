from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('datos/<str:username>', views.datos),
    path('project/', views.project),
    path('task/<int:id>', views.task),
    
]
