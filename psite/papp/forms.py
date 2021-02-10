from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tasks
from django.forms import ModelForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CustomLoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        exclude = ['id','userid']

