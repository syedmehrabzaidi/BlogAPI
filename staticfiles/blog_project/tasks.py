from django.core.mail import send_mail

from blog_project.celery import app
from blog_project import settings


@app.task
def send_mail_func(user_id):
    # from django.contrib.auth.models import User
    from settings import AUTH_USER_MODEL as User

    user = User.objects.get(id=user_id)
    usernames = user.profile.follower.all().values_list('username', flat=True)
    followers = user.profile.follower.all().values_list('email', flat=True)

    # for follower in user.profile.follower.all():
    send_mail(
            subject=f'Hi  post a blog',
            message='msg of mail',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['mehrab@gmail.com'],
            fail_silently=True,
        )
