from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader,RequestContext
from .models import Tasks,Comments
from .forms import TaskForm, CustomUserCreationForm, CustomLoginForm
from django.shortcuts import render, redirect,reverse
from datetime import datetime

def home(request):
    template = loader.get_template('base.html')
    context = {
    }
    return HttpResponse(template.render(context))

def test(request):
    context = {}
    return render(request, 'include.html',context)

def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            status = "Success"
            return render(request,'tasks/tasks.html', {'form':form,'status':status})
        else:
            form = TaskForm()
            status = "Error"
        return render(request,'comment.html', {'form':form,'status':status})
    elif request.method == 'GET':
        template = loader.get_template('tasks/tasks.html')
        task_list = Tasks.objects.order_by('name')[:5]
        context = {
            'form':TaskForm(),
            'task_list':task_list
        }
        return render(request,'tasks/tasks.html',context)


def matrix(request):
    tasks_list = Tasks.objects.order_by('due')[:5]
    template = loader.get_template('matrix.html')
    context = {'tasks': tasks_list}
    return HttpResponse(template.render(context))


def welcome(request):
    template = loader.get_template('welcome.html')
    context = {}
    return HttpResponse(template.render(context))

def task_list(request):
    tasks_list = Tasks.objects.order_by('due')[:5]
    template = loader.get_template('tasks/tasks.html')
    context = {'tasks': tasks_list}
    return HttpResponse(template.render(context))


'''
Start of user signin views
'''
def register(request):
    '''
    if request.user.is_authenticated:
        return redirect('../../home', username=request.user.username)
    '''
    if request.method == "GET":
        form = CustomUserCreationForm(request.GET)
        form.fields['username'].initial = "123"
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("../home"))
        else:
            return render(request,'registration/register.html',{"form":form})
