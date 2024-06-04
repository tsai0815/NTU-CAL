from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.category} {self.description}"

class Solution(models.Model):
    description = models.CharField(max_length=300)
    question = models.ForeignKey(Question, related_name='solutions', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.description} {self.question}"



