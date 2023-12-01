from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm, UserLoginForm, ToDoForm
from .models import ToDo, CustomUser


def register(request):
    if request.method == 'POST':
        # if method is post
        form = UserRegistrationForm(request.POST)
        # UserRegistrationForm --> forms.py
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'tasks/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        # UserLoginForm --> forms.py
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # dashboard.html
    else:
        form = UserLoginForm()
    return render(request, 'tasks/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')  # login.html


def dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to the login page
        return redirect('login')  # login.html

    tasks = ToDo.objects.filter(user=request.user)  # if a user is login then it will show all tasks available.
    return render(request, 'tasks/dashboard.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = ToDoForm()
    return render(request, 'tasks/create_task.html', {'form': form})


def update_task(request, task_id):
    task = get_object_or_404(ToDo, id=task_id, user=request.user)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ToDoForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(ToDo, id=task_id, user=request.user)
    task.delete()
    return redirect('dashboard')


def user_profile(request):
    user = CustomUser.objects.get(username=request.user)
    return render(request, 'tasks/user_profile.html', {'user': user})
