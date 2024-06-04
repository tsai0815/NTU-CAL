from django import forms
from .models import Question, Solution

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

class SolutionForm(forms.ModelForm):

    class Meta:
        model = Solution
        fields = ['description']

