from django.db import models
from django.utils import timezone,dateformat
from datetime import datetime, timedelta
import uuid
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User


class Projects(models.Model):
    name = models.CharField(max_length=100, default='Test', unique=True)
    description = models.CharField(max_length=1000, default='Test')
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    priority = models.CharField(max_length=20,default = 'Delete')

    def __str__(self):
        return "Project Object"


class Tasks(models.Model):

    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='name')
    description = models.CharField(max_length=1000, default = 'Test')
    priority = models.CharField(max_length=100, choices = ([]))
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, blank = True)
    project = models.CharField(max_length=100, blank = True, default="*", choices=([(p.name, p.name) for p in Projects.objects.all()]))
    '''
    project = models.CharField(max_length=100,
                               choices=([(p.name, p.name) for p in Projects.objects.all()]), blank=True,
                               default="*")
   
    '''
    #the first object is what you save it as, the second is what it displaysa s
    due = models.DateTimeField(default = timezone.now)
    critical_path = models.BooleanField(default='False')
    time_required = models.DurationField(default=timedelta(hours=1))
  #  user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return "Task Object"



class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    text = models.CharField(max_length = 200)
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return "Comment"
