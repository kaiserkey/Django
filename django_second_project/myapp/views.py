from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Re
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def hello(request):
    return HttpResponse("<h1 style='color: blue'>Hello World</h1>")

def about(request):
    return HttpResponse("<h1 style='color: green'>About</h1>")

def datos(request, username):
    print(username)
    return HttpResponse("<h1 style='color: red'>Usuario: " + username + "</h1>")

def project(request):
    projects = Project.objects.all()
    return JsonResponse({"projects": list(projects.values())})

def task(request, id):
    #tasks = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return JsonResponse({"tasks": task.title})
