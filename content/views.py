from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    context = {'page': 'Home Page'}
    return render(request, 'home.html', context)


def contact(request):
    contact_obj = Contact.objects.all()
    print(contact_obj)
    context = {'page': 'Contact page', 'contacts': contact_obj}
    return render(request, 'contact.html', context)


def dynamic(request, id):
    print(id)
    context = {'page': f'Dynamic Page{id}', 'id': id}
    return render(request, 'dynamic.html', context)

@login_required(login_url='/login_page/')
def todo(request):
    print(request.user)
    if request.method == 'POST':
        task = request.POST.get('task')
        print(task)
        if task is not None:
            task_obj = Todo(task_name=task, user= request.user)
            task_obj.save()
        return redirect('/todo/')
    # tasks = Todo.objects.all()
    tasks=Todo.objects.filter(user =request.user)
    context = {'tasks': tasks}
    return render(request, 'todo.html', context)


def delete_task(request, id):
    try:
        task = Todo.objects.get(id=id)
        task.delete()
    except Todo.DoesNotExist:
        pass
    return redirect('/todo/')


def mark_as_completed(request, id):
    try:
        task = Todo.objects.get(id=id)
        task.is_complete = True
        task.save()
    except Todo.DoesNotExist:
        pass
    return redirect('/todo/')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user =User.objects.filter(email=email).first()
        print(user)
        print(password)
        if user is None:
            messages.success(request, 'User not found')

            return redirect('/login_page/')
        user_auth =authenticate(username=email,password=password)

        if user_auth:
            login(request,user)
            return redirect('/todo')
        print(user_auth)

    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(email=email, password=password, username=email)
        user.set_password(password)
        user.save()
    return render(request, 'register.html')
