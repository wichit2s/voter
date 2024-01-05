from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('questions/', views.questions, name='questions'),
    path('search/', views.search, name='search'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('htmx/search', views.htmx_search, name='search'),
]
