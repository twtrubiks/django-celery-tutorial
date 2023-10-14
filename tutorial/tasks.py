from celery import shared_task, signals
from django.core.mail import send_mail


@shared_task(ignore_result=True)
def task_mail():
    subject = "celery subject test"
    message = "celery message test"
    recipient = ["xxxxxx@gmail.com", "xxxxxx@gmail.com", "xxxxxx@yahoo.com.tw"]
    send_mail(
        subject,
        message,
        "admin@celery_test.com",
        recipient,
    )

@shared_task(ignore_result=True, bind=True)
def task_mail_retry(self):
    try:
        if 1:
            raise Exception()

        subject = "celery subject test"
        message = "celery message test"
        recipient = ["xxxxxx@gmail.com", "xxxxxx@gmail.com", "xxxxxx@yahoo.com.tw"]
        send_mail(
            subject,
            message,
            "admin@celery_test.com",
            recipient,
        )

    except Exception as e:
        raise self.retry(exc=e, countdown=3)


@signals.task_prerun.connect
def prerun_task_mail(task_id, task, *args, **kwargs):
    print(f"task_id: {task_id},  task: {task}")
    print("prerun_task_mail ......")

@signals.task_postrun.connect
def postrun_task_mail(task_id, task, *args, **kwargs):
    print(f"task_id: {task_id},  task: {task}")
    print("postrun_task_mail ......")

@signals.task_success.connect
def success_task_mail(sender=None, **kwargs):
    print(sender)
    print("success_task_mail ......")

@signals.task_failure.connect
def failure_task_mail(task_id, exception, *args, **kwargs):
    print(f"task_id: {task_id},  exception: {exception}")
    print("failure_task_mail ......")