from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

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
    return JsonResponse

def task(request):
    return HttpResponse("<h1 style='color: black'>Project</h1>")