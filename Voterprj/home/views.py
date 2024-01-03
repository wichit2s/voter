from django.shortcuts import render
from vote import models

# Create your views here.
def home(req):
    return render(req, 'home/home.html')

def questions(req):
    context = {
            'questions': models.Question.objects.all()
    }
    return render(req, 'home/questions.html', context)
