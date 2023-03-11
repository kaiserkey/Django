from django.shortcuts import render
from myfirstapp.models import Post

# Create your views here.
def home(request):
    return render(request, 'post/index.html',
                    {'posts': Post.objects.count(),
                    'message': 'Hello World'
                    })
