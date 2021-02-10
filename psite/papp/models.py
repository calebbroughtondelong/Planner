from django.db import models
from django.utils import timezone,dateformat
from datetime import datetime
import uuid
from urllib import request


def get_current_user(request):
    current_user = request.user
    return current_user
class Tasks(models.Model):

    name = models.CharField(max_length=100, default='Test')
    text = models.CharField(max_length=500, default = 'Test')
    priority = models.CharField(max_length=20,default = 'Delete')
    project = models.CharField(max_length=50)
    due = models.DateTimeField(default = timezone.now)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    userid = models.CharField(max_length=100, default = '0')
    #HOw to save user id

    def __str__(self):
        return "Task Object"




class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    text = models.CharField(max_length = 200)
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return "Comment"
