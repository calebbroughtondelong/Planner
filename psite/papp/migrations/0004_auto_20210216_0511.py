# Generated by Django 3.1.6 on 2021-02-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0003_tasks_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='project',
            field=models.CharField(blank=True, choices=[('*', ' '), ('First', 'First')], default='*', max_length=100),
        ),
    ]
