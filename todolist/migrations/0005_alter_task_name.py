# Generated by Django 3.2.9 on 2022-06-12 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20220612_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
