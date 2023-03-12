from django.urls import path
from . import views, admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('about/', views.about)
]
