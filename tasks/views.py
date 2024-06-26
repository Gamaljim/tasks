from django.shortcuts import render, redirect
from .models import Task, SubTask
from .forms import TaskForm , TaskUpdateForm, SubTaskForm, SubTaskUpdateForm

from django.utils import timezone
from datetime import timedelta

# Create your views here.
def home_page(request):
    tasks = Task.objects.all().order_by("-id")
    done_tasks = tasks.filter(status='Done')

    three_days_ago = timezone.now().date() - timedelta(days=3)
    tasks_done_before = tasks.filter(completed_at__date=three_days_ago)

    today_time = timezone.now().date()
    tasks_created_today = tasks.filter(created_at__date=today_time)
    context = {
        'tasks':tasks,
        'done_tasks':done_tasks,
        'three_days_ago':tasks_done_before,
        'created_today':tasks_created_today
    }
    return render(request, "tasks/home.html", context=context)



def create_task(request):
    #CRUD
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            new_task = Task.objects.create(title=title, description=description)
            return redirect('home') 
    else:
        form = TaskForm()

    return render(request, "tasks/add_task.html", {"form": form})




def get_task(request, pk):

    task = Task.objects.get(id=pk)
    # sub_tasks = SubTask.objects.filter(related_task=task)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, 'tasks/view_task.html', {'task':task, "form":form, 'items':task.items.all()})




def delete_task(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect('home')




#CREATING CRUD FOR SUB-TASK
def create_sub_task(request):
    #C
    if request.method == "POST":
        form = SubTaskForm(request.POST)
        if form.is_valid():
            new_sub_task= form.save()
            return redirect('view', pk=new_sub_task.related_task.id)
    else:
        form = SubTaskForm()

    return render(request, "tasks/add_sub_task.html", {"sub_form":form})



def get_sub_task(request, pk):
    sub_task = SubTask.objects.get(id=pk)
    if request.method == 'POST':
        form = SubTaskUpdateForm(request.POST, instance=sub_task)
        if form.is_valid():
            form.save()
    else:
        form = SubTaskUpdateForm(instance=sub_task)

    return render(request , "tasks/view_subtask.html", {'sub_task':sub_task, 'form':form})

def delete_sub_task(request, pk):
    sub_task = SubTask.objects.get(id=pk)
    task = sub_task.related_task.id
    sub_task.delete()
    return redirect('view', pk=task)
