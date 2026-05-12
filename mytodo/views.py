from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task

@login_required
def home(request):
    if request.method == 'POST':
        new_title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        
        if new_title:
            Task.objects.create(title=new_title, user=request.user, date_due=due_date)
            return redirect('home')
    
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'index.html', {'tasks': tasks})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return redirect('home')

@login_required
def complete_task(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.completed = True
    task.save()
    return redirect('home')

@login_required
def edit_task(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.date_due = request.POST.get('due_date')
        task.save()
        return redirect('home')
    return render(request, 'edit_task.html', {'task': task})
