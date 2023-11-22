from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from vote.models import *

# Create your views here.
def home(req):
    return render(req, 'vote/home.html', {
        'questions': Question.objects.all()
    })

def login(req):
    message = ''
    next_url = req.GET.get('next')
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        next_url = req.POST.get('next_url')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(req, user)
            return redirect(next_url) 
        else:
            message = 'login fails!!!'
    elif next_url:
        message = 'ลงชื่อเข้าใช้งานก่อน ไปหน้า ' + next_url
    else:
        next_url = 'vote_home'

    return render(req, 'vote/login.html', { 'message': message, 'next_url': next_url })

def logout(req):
    auth_logout(req)
    return redirect('vote_home')

@login_required(login_url='/vote/login')
def make_question(req):
    form = QuestionForm()
    if req.method == 'POST':
        form = QuestionForm(req.POST)
        if form.is_valid():
            form.save()

    return render(req, 'vote/make_question.html', { 
        'form': form,
     })

@login_required(login_url='/vote/login')
def answer_question(req):
    form = AnswerForm()
    if req.method == 'POST':
        form = AnswerForm(req.POST)
        if form.is_valid():
            form.save()

    return render(req, 'vote/answer_question.html', { 
        'form': form,
     })

@login_required(login_url='/vote/login')
def create_answer(req):
    if req.method == 'POST':
        qid = int(req.POST.get('question_id'))
        question = get_object_or_404(Question, pk=qid)
        text = req.POST.get('text').strip().lower()
        if text:
            answer, created = Answer.objects.get_or_create(user=req.user, question=question, text=text)
            answer.count += 1
            answer.save()
            
    return redirect('vote_home')

@login_required(login_url='/vote/login')
def create_question(req):
    return redirect('vote_home')
