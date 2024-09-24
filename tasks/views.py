from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks, 'form': form}
    )


def task_edit(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(
        request,
        'tasks/task_edit.html',
        {'form': form, 'task': task}
    )

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')