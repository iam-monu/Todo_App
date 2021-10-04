from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('todo/', todo, name="todo"),
    path('dynamic/<id>', dynamic, name="dynamic"),
    path('delete_task/<id>', delete_task, name="delete_task"),
    path('mark_as_completed/<id>', mark_as_completed, name="mark_as_completed"),

    path('login_page/', login_page, name="login_page"),
    path('register_page/', register_page, name="register_page"),


]
