from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , max_length=15,  null=True, blank=True)
    task_name = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name + 'created by' + self.user.username