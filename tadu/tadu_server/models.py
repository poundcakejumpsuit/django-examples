from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    join_date = models.DateTimeField('join date', default=timezone.now)
    

class Task(models.Model):
    task_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=300)
    entry_date = models.DateTimeField('entry date')
    due_date = models.DateTimeField('due date')

    def __str__(self):
        return self.task_text