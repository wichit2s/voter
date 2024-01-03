from django.urls import path, include
from vote import views

urlpatterns = [
    path('', views.home, name='vote_home'),
    path('make_question/', views.make_question, name='vote_make_question'),
    path('answer_question/', views.answer_question, name='vote_answer_question'),

    path('login/', views.login, name='vote_login'),
    path('logout/', views.logout, name='vote_logout'),

    path('create_question/', views.create_question, name='vote_create_question'),
    path('create_answer/', views.create_answer, name='vote_create_answer'),
]
