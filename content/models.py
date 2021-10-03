from django.db import models


# Create your models here.

class Contact(models.Model):
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()


class Todo(models.Model):
    task = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
