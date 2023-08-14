from django.db import models

# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=40)
    taskDescription = models.CharField(max_length=50)
    is_completed = models.BooleanField(default = False)
    