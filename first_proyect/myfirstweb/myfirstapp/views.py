from django.shortcuts import render
from myfirstapp

# Create your views here.
def home(request):
    return render(request, 'post/index.html',
                    {'title': 'Home', 'content': 'Welcome to the home page!'})
