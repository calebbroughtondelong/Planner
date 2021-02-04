from django.db import models
from django.utils import timezone,dateformat


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    due = models.DateTimeField(default = timezone.now)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return "Task Object"

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    text = models.CharField(max_length = 200)
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return "Comment"
