from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def task_mail():
    subject = 'subject test'
    message = 'message test'
    mail_sent = send_mail(subject,
                          message,
                          'admin@celery_test.com',
                          ['xxxxxx@gmail.com',
                           'xxxxxx@gmail.com',
                           'xxxxxx@yahoo.com.tw'])
    return mail_sent
