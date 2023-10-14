from django.contrib import admin
from django.urls import path
from tutorial import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('task_use_celery/', views.task_use_celery, name='task_use_celery'),
    path('task_not_use_celery/', views.task_not_use_celery, name='task_not_use_celery'),

]