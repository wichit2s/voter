from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from vote.models import *

# Create your views here.
def home(req):
    return render(req, 'vote/home.html', {
        'question': Question.objects.all()
    })

def login(req):
    return render(req, 'vote/login.html')

@login_required(login_url='/vote/login')
def make_question(req):
    return render(req, 'vote/make_question.html')

@login_required(login_url='/vote/login')
def answer_question(req):
    return render(req, 'vote/answer_question.html')