from __future__ import unicode_literals 
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import python_4_unicode_compatible
# Create your models here.
@python_4_unicode_compatible
class Post(models.Model):
    STATUS = (  ('draft','Draft'),
                ('published','Published'))
    title = models.CharField(max_length=100)
    sulug = models.SlugField(max_length=100,unique_for_date='publish', unique=True, help_text=("A label for URL config."))
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    publish = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-publish',)
