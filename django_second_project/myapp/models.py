from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)