# Generated by Django 3.2.9 on 2022-06-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0021_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='Open', max_length=20),
        ),
    ]
