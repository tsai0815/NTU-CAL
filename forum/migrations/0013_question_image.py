# Generated by Django 5.0.6 on 2024-06-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_remove_question_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='calculus/'),
        ),
    ]
