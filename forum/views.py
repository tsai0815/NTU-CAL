from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Question
from .forms import QuestionForm


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def topics_listing(request):
    template = loader.get_template('topics-listing.html')
    return HttpResponse(template.render())

def topics_detail(request):
    template = loader.get_template('topics-detail.html')
    return HttpResponse(template.render())

def buy_coffee(request):
    template = loader.get_template('buy-coffee.html')
    return HttpResponse(template.render())

def aboutus(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render())

def account_center(request):
    template = loader.get_template('account-center.html')
    return HttpResponse(template.render())

def calculus(request):
    template = loader.get_template('calculus.html')
    return HttpResponse(template.render())


def calculus_ask(request):    
    template = loader.get_template('calculus-ask.html')
    form = QuestionForm(request.POST or None)

    # form = QuestionForm()
    
    if form.is_valid():
        obj = Question.objects.create(
            title = form.cleaned_data.get('title'),
            category = form.cleaned_data.get('category'),
            description = form.cleaned_data.get('description')
        )
        redirectTemplate = loader.get_template('calculus.html')
        return HttpResponse(redirectTemplate.render())


    context = {
        'form': form
    }
    return render(request, "calculus-ask.html", context)
  
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
