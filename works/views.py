from django.shortcuts import render,redirect
from works.models import TaskModel
from works.forms import TaskForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def add_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            print(task.cleaned_data)
            task.save()
            return redirect('show_task')
    else:
        task = TaskForm()
    return render(request, 'addtask.html', {'form': task})


def show_task(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_task.html', {'tasks' : tasks})

def delete_task(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('show_task')

def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    return render(request, 'addtask.html', {'form':form})

def com_task(request, id):
    tasks = TaskModel.objects.get(pk=id)
    tasks.is_completed = True
    task = TaskModel.objects.all()
    tasks.save()
    return render(request, 'com_task.html', {'tasks':task})

def delete_task_com(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    task = TaskModel.objects.all()
    return render(request, 'com_task.html', {'tasks':task})



