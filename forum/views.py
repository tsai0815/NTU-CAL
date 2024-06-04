from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Question, Solution
from .forms import QuestionForm, SolutionForm, SignUpForm, SignInForm

from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

def main(request):
    context = {'is_authenticated': request.user.is_authenticated}
    return render(request, 'main.html', context)

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

@login_required(login_url='/login/')
def account_center(request):
    template = loader.get_template('account-center.html')
    return HttpResponse(template.render())

@login_required(login_url='/login/')
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

        like_action = request.POST.get('like_action')
        if like_action:
            if like_action == 'like':
                solution.likes.add(request.user)
            elif like_action == 'dislike':
                solution.dislikes.add(request.user)

        solution.save()
        return redirect('calculus')
    else:
        print(form.errors)
    return render(request, 'calculus.html', {'questions': questions, 'form': form})


@login_required(login_url='/login/')
def calculus_ask(request):    
    # template = loader.get_template('calculus-ask.html')
    form = QuestionForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        obj = Question.objects.create(
            title = form.cleaned_data.get('title'),
            category = form.cleaned_data.get('category'),
            description = form.cleaned_data.get('description'),
            image = form.cleaned_data.get('image')
        )
        return redirect('calculus')


    context = {
        'form': form,
    }
    return render(request, "calculus-ask.html", context)
  

def login_view(request):
    if request.method == 'POST':
        next_url = request.POST.get('next', '/calculus')
        if 'signup' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return JsonResponse({'status': 'success'}, status=200)
            else:
                return JsonResponse({'status': 'fail', 'errors': form.errors.as_json()}, status=400)
        elif 'signin' in request.POST:
            form = SignInForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                User = get_user_model()
                try:
                    username = User.objects.get(email=email).username
                except User.DoesNotExist:
                    return JsonResponse({'status': 'fail', 'errors': {'__all__': [{'message': 'Invalid email or password', 'code': 'invalid_login'}]}}, status=400)

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return JsonResponse({'status': 'success', 'next': next_url}, status=200)
                else:
                    return JsonResponse({'status': 'fail', 'errors': {'__all__': [{'message': 'Invalid email or password', 'code': 'invalid_login'}]}}, status=400)
            else:
                return JsonResponse({'status': 'fail', 'errors': form.errors.as_json()}, status=400)
        else:
            return JsonResponse({'status': 'invalid'}, status=400)
    else:
        next_url = request.GET.get('next', '/calculus')
        return render(request, 'login.html', {'next': next_url})
