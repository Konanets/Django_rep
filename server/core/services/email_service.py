import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from .jwt_service import ActivateToken, JWTService, ResetPasswordViaEmailToken
from configs.celery import app

from apps.users.models import UserModel as User
from django.contrib.auth import get_user_model

UserModel: User = get_user_model()


class EmailService:
    @staticmethod
    @app.task
    def __send_email(to: str, template_name: str, context: dict, subject: str):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def register_email(cls, user):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email.delay(user.email, 'register.html',
                               {'name': user.profile.name,
                                'surname': user.profile.surname,
                                'url': url},
                               'Register')

    @classmethod
    def reset_password_via_email(cls, user):
        token = JWTService.create_token(user, ResetPasswordViaEmailToken)
        url = f'http://localhost:3000/reset_password/{token}'
        data = {
            'name': user.profile.name,
            'surname': user.profile.surname,
            'url': url
        }
        cls.__send_email(user.email, 'reset.html', data, 'Reset')

    @staticmethod
    @app.task
    def spam():
        for user in UserModel.objects.all():
            EmailService.__send_email(user.email, 'spam.html', {},'spam')
