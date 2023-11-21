from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from vote.models import *

# Create your views here.
def home(req):
    return render(req, 'vote/home.html', {
<<<<<<< HEAD
        'questions': Question.objects.all()
=======
        'question': Question.objects.all()
>>>>>>> 069a687a8466ced61d59dca31d2c3200254ad792
    })

def login(req):
    return render(req, 'vote/login.html')

@login_required(login_url='/vote/login')
def make_question(req):
    return render(req, 'vote/make_question.html')

@login_required(login_url='/vote/login')
def answer_question(req):
    return render(req, 'vote/answer_question.html')