from django.http import HttpResponse
from django.shortcuts import render, redirect
from vote import models
from home.models import Notification
from django.db.models import Q
from django.contrib import auth
import pygwalker as pyg
import pandas as pd
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.
def home(req):
    #return render(req, 'home/home.html')
    context = {
        'notifications': [],
    }
    if req.user.is_authenticated:
        context['notifications'] = Notification.objects.filter(user=req.user)
    return render(req, 'home/notification.html', context)

@user_passes_test(lambda user: user.is_superuser, login_url='login')
def dashboard(req):
    d = {
        'usernames': [],
        'questions': [],
        'answers': [],
     }
    for q in models.Question.objects.all():
        d['usernames'].append(q.user.username)
        d['questions'].append(q.text)
        d['answers'].append(q.answer_set.count())

    df = pd.DataFrame(d)
    context = {
        #'questions': models.Question.objects.all(),
        'dashboard': pyg.to_html(df),
    }
    return render(req, 'home/dashboard.html', context)

def questions(req):
    context = {
        'questions': models.Question.objects.all()
    }
    return render(req, 'home/questions.html', context)

@login_required(login_url='login')
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

def htmx_notification_delete(req, id):
    #print(f'htmx_notification_delete({id})')
    n = Notification.objects.filter(pk=id).first()
    if n:
        n.delete()
    return HttpResponse('')

def htmx_notification_count(req):
    #print(f'htmx_notification_count({req.user})')
    if req.user.is_authenticated:
        return HttpResponse(f'{req.user.notification_set.count()}')
    return HttpResponse('0')

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
