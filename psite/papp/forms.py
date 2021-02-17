from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tasks,Projects
from django.forms import ModelForm
from django import forms
import uuid
from django.shortcuts import render, redirect,reverse
from django.utils.safestring import mark_safe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CustomLoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

class TaskForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super(TaskForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_show_errors = True

        self.helper.add_input(Submit('submit', 'Submit'))

        self.fields['project'].choices = ([(" ", " ")] + [(p.name,p.name) for p in Projects.objects.all()])
        priority_choices = ([("JDI","JDI"),("UI", "UI"), ("U", "U"), ("I", "I"), ("D", "D")])
        self.fields['priority'] = forms.ChoiceField(choices = priority_choices)

    class Meta:
        model = Tasks
        exclude = ['id','userid','project_id']

class ProjectForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_show_errors = True

        self.helper.add_input(Submit('submit', 'Submit'))

        priority_choices = ([("JDI", "JDI"), ("UI", "UI"), ("U", "U"), ("I", "I"), ("D", "D")])
        self.fields['priority'] = forms.ChoiceField(choices=priority_choices)



    class Meta:
        model = Projects
        exclude = ['project_id']