from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('todo/', todo, name="todo"),
    path('dynamic/<id>', dynamic, name="dynamic")
]
