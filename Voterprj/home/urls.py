from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('questions/', views.questions, name='questions'),
    path('search/', views.search, name='search'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('htmx/search', views.htmx_search, name='htmx_search'),
    path('htmx/notification/delete/<int:id>/', views.htmx_notification_delete, name='htmx_notification_delete'),
    path('htmx/notification/count/', views.htmx_notification_count, name='htmx_notification_count'),
]
