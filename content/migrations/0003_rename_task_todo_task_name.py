# Generated by Django 3.2.7 on 2021-10-03 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='task',
            new_name='task_name',
        ),
    ]