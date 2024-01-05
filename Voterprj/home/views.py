from django.shortcuts import render, redirect
from vote import models
from django.db.models import Q
from django.contrib import auth

# Create your views here.
def home(req):
    return render(req, 'home/home.html')

def questions(req):
    context = {
            'questions': models.Question.objects.all()
    }
    return render(req, 'home/questions.html', context)

def search(req):
    print('search()')
    return render(req, 'home/search.html')

def htmx_search(req):
    print('htmx_search()')
    context = {
            'questions': None,
        }
    if req.method == 'POST':
        search = req.POST.get('search', '')
        context['questions'] = models.Question.objects.filter(
                Q(text__icontains=search)
                | Q(user__username__icontains=search)
                )

    return render(req, 'home/htmx/search.html', context)

def login(req):
    message = ''
    if req.user.is_authenticated:
        return redirect('home')

    elif req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(req, user)
            return redirect('home') 
        else:
            message = 'login fails!!!'

    return render(req, 'home/login.html', { 'message': message })

def logout(req):
    auth.logout(req)
    return redirect('home')
