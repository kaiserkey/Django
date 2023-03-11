from django.conf.urls import urls
from .views import home

urlpatterns = [
    urls(r'^$', home, name='home'),
]
