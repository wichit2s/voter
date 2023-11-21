from django.urls import path
from vote import views

urlpatterns = [
    path('', views.home, name='vote_home'),
    path('make_question/', views.make_question, name='vote_make_question'),
    path('answer_question/', views.answer_question, name='vote_answer_question'),
    path('login/', views.login, name='vote_login'),
]