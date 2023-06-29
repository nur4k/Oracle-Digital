from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task
def send_mail_to_email(email, url):
    data = {
        "email": email,
        "message": "Для заверщения регистрации перейдите по ссылке",
        "url": url,
    }
    html_body = render_to_string("index.html", data)
    msg = EmailMultiAlternatives(subject="Здравствуйте", to=[email])
    msg.attach_alternative(html_body, "text/html")
    msg.send()
