from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tasks,Projects
from django.forms import ModelForm
from django import forms
import uuid
from django.shortcuts import render, redirect,reverse

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CustomLoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

class TaskForm(ModelForm):

    def __init__(self):
        super(TaskForm,self).__init__()
        self.fields['project'].choices = ([("*", " ")] + [(p.name,p.name) for p in Projects.objects.all()])
        self.fields['priority'].choices = ([("1","UI"),("2","U"),("3","I"),("4","D")])

    class Meta:
        model = Tasks
        exclude = ['id','userid','project_id']



class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        exclude = ['project_id']