from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm , TaskUpdateForm

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
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, 'tasks/view_task.html', {'task':task, "form":form})




def delete_task(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect('home')