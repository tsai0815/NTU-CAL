# Generated by Django 5.0.6 on 2024-05-29 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_solution_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='slug',
        ),
    ]