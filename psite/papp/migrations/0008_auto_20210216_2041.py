# Generated by Django 3.1.6 on 2021-02-17 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0007_tasks_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='priority',
            field=models.CharField(choices=[], max_length=100),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='project',
            field=models.CharField(blank=True, default=' ', max_length=100),
        ),
    ]