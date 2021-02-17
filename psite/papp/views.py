from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader,RequestContext
from .models import Tasks,Comments,Projects
from .forms import TaskForm, CustomUserCreationForm, CustomLoginForm, ProjectForm
from django.shortcuts import render, redirect,reverse
from datetime import datetime
import uuid

def home(request):
    template = loader.get_template('base.html')
    context = {
    }
    return HttpResponse(template.render(context))

def test(request):
 #   pass
    Tasks.objects.all().delete()
    return redirect(reverse('home'))

def tasks(request):
    task_list = Tasks.objects.order_by('name')[:5]
    project_list = Projects.objects.order_by('name')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)

        project_selected = request.POST.get('project')
        if Projects.objects.filter(name=project_selected):
            associated_project = Projects.objects.filter(name=project_selected)[0]
            form.instance.project_id = str(associated_project.project_id)
            form.instance.project = associated_project.name

        if form.is_valid():
            form.save()
            status = "Success"
            form = TaskForm()
            return render(request,'tasks/tasks.html', {'form':form,'status':status,'task_list':task_list})
        else:
            context = {
                'form': form,
                'task_list': task_list,
                'project_list': project_list,
                'status':"Did not work"
            }

            return render(request, 'tasks/tasks.html', context)
      # return render(request,'tasks/tasks.html', {'form':form,'status':status})
    elif request.method == 'GET':

        context = {
            'form': form,
            'task_list':task_list,
            'project_list': project_list,
        }
        return render(request,'tasks/tasks.html',context)

def projects(request):
    project_list = Projects.objects.order_by('name')
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            content = {
                'status' : 'Success',
                'form': form,
                'project_list': project_list,
            }

            return render(request,'tasks/projects.html', )
        else:
            form = ProjectForm()
            status = "Error"
        return render(request,'tasks/projects.html', {'form':form,'status':status})
    elif request.method == 'GET':
        context = {
            'form':form,
            'project_list':project_list,
            'projects': projects,
        }
        return render(request,'tasks/projects.html',context)


def matrix(request):
    tasks_list = Tasks.objects.order_by('due')[:5]
    template = loader.get_template('matrix.html')
    context = {'tasks': tasks_list}
    return HttpResponse(template.render(context))


def welcome(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    template = loader.get_template('welcome.html')
    context = {}
    return HttpResponse(template.render(context))

def task_list(request):
    tasks_list = Tasks.objects.order_by('due')[:5]
    template = loader.get_template('tasks/tasks.html')
    context = {'tasks': tasks_list}
    return HttpResponse(template.render(context))

def getbyid(request):
    if request.method == 'GET':
        project_list = Projects.objects.order_by('name')
        context = {
            'form':ProjectForm(),
            'project_list':project_list,
            'projects': projects,
        }
        return render(request,'basic/getbyid.html',context)

    items = Projects.objects.order_by('name')
    return render(request, 'basic/getbyid.html', {'item':items})




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

