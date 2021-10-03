from django.http import HttpResponse
from django.shortcuts import render
from .models import *


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


def todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        print(task)
        if task is not None:
            task_obj = Todo(task=task)
            task_obj.save()
    return render(request, 'todo.html')
