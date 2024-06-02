from django import forms
from .models import Question, Solution
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

class SolutionForm(forms.ModelForm):

    class Meta:
        model = Solution
        fields = ['description'] 

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SignInForm(AuthenticationForm):
    username = forms.EmailField(label='Email')