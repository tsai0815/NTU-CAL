# Generated by Django 5.0.6 on 2024-05-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_remove_solution_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
