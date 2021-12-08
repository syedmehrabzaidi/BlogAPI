from django.core.mail import send_mail

from blog_project.celery import app
from blog_project import settings


@app.task
def send_mail_func(user_id):
    send_mail(
        subject=f'Hi {user_id.name}  post a blog',
        message='msg of mail',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['mehrab@gmail.com'],
        fail_silently=True,
    )
