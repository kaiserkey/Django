from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)