# Generated by Django 3.2.9 on 2022-06-12 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_rename_name_task_t_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='t_name',
        ),
    ]
