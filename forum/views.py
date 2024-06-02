from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Question, Solution
from .forms import QuestionForm, SolutionForm, SignUpForm, SignInForm

from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User

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
    questions = Question.objects.all()

    form = SolutionForm(request.POST)
    if form.is_valid():
        # obj = Solution.objects.create(
        #     description = form.cleaned_data.get('description'),
        #     question = form.cleaned_data.get('question')
        # )
        solution = form.save(commit=False)
        question_id = request.POST.get('question_id')
        solution.question_id = question_id
        solution.save()
        return redirect('calculus')
    else:
        print(form.errors)

    return render(request, 'calculus.html', {'questions': questions, 'form': form})


def calculus_ask(request):    
    # template = loader.get_template('calculus-ask.html')
    form = QuestionForm(request.POST or None)
    
    if form.is_valid():
        obj = Question.objects.create(
            title = form.cleaned_data.get('title'),
            category = form.cleaned_data.get('category'),
            description = form.cleaned_data.get('description')
        )
        return redirect('calculus')


    context = {
        'form': form,
    }
    return render(request, "calculus-ask.html", context)
  

def login_view(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return JsonResponse({'status': 'success'}, status=200)
            else:
                return JsonResponse({'status': 'fail', 'errors': form.errors}, status=400)
        elif 'signin' in request.POST:
            form = SignInForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return JsonResponse({'status': 'success'}, status=200)
            return JsonResponse({'status': 'fail', 'errors': form.errors}, status=400)
    else:
        # 如果是GET請求，渲染login.html模板
        return render(request, 'login.html')