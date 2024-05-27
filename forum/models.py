from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title} {self.category} {self.description}"
