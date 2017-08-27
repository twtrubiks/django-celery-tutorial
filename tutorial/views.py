from django.core.mail import send_mail
from django.shortcuts import render

from tutorial.tasks import task_mail


# Create your views here.

def dashboard(request):
    return render(request,
                  'tutorial/dashboard.html')


def task_use_celery(request):
    task_mail.delay()
    return render(request,
                  'tutorial/process_done.html')


def task_not_use_celery(request):
    subject = 'subject test'
    message = 'message test'
    recipient = ['xxxxxx@gmail.com',
                 'xxxxxx@gmail.com',
                 'xxxxxx@yahoo.com.tw']
    send_mail(subject,
              message,
              'admin@celery_test.com',
              recipient)
    return render(request,
                  'tutorial/process_done.html')
