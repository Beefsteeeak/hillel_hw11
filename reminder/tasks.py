from celery import shared_task

from django.core.mail import send_mail as celery_send_email


@shared_task
def send_email(subject, message, to_email):
    celery_send_email(subject, message, 'admin@mail.com', [to_email])
