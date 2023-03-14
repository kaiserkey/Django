from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    title = "Welcome to the index of my blog"
    return render(request, "index.html", {"title": title})????????/asdasdasdasd


def about(request):
    return render(request, "about.html")

def datos(request, username):
    print(username)
    return HttpResponse("<h1 style='color: red'>Usuario: " + username + "</h1>")

def project(request):
    projects = Project.objects.all()
    return render(request, "project.html", {"projects": projects})

def task(request):
    tasks = Task.objects.all()
    #task = get_object_or_404(Task, id=id)
    return render(request, "task.html", {"task": tasks})
