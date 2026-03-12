from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('tasks/', views.create_task, name='create_task'),
    path('tasks/list/', views.list_tasks, name='list_tasks'),
]
