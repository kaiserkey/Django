from django.urls import path
from .views import home, posts

urlpatterns = [
    path('home', home),
    path('posts', posts)
]
