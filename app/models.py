from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, help_text="Name of the task")
    description = models.TextField(help_text="Description of your task")
    completed = models.BooleanField(default=False, help_text="Is the task open?")
    created = models.DateTimeField(auto_now_add=True, help_text='Created time')
