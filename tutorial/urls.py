from django.conf.urls import url

from tutorial import views

urlpatterns = [

    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^task_use_celery/', views.task_use_celery, name='task_use_celery'),
    url(r'^task_not_use_celery/', views.task_not_use_celery, name='task_not_use_celery'),

]
