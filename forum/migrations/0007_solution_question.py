# Generated by Django 5.0.6 on 2024-05-29 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_remove_solution_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='forum.question'),
        ),
    ]