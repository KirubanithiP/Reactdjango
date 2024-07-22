# tasks.py

from celery import shared_task
from django.core.mail import send_mail
from reactdjango.settings import EMAIL_HOST_USER 

@shared_task
def send_email_task(email, subject, message):
    send_mail(subject, message,EMAIL_HOST_USER, [email])
