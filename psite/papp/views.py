from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader,RequestContext
from .models import Tasks,Comments
from .forms import TaskForm
from django.shortcuts import render, redirect

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
        form.id = 1
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = TaskForm()
        return render(request,'comment.html', {'form':form})
    elif request.method == 'GET':
        template = loader.get_template('tasks.html')
        HttpResponse("Test")
        context = {
            'form':TaskForm
        }
        return render(request,'tasks.html',context)


def matrix(request):
    tasks_list = Tasks.objects.order_by('due')[:5]
    template = loader.get_template('matrix.html')
    context = {'tasks': tasks_list}
    return HttpResponse(template.render(context))

def generate_task_id():
    pass