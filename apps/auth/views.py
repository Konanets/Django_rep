from core.services.email_service import ActivateToken, EmailService, ResetPasswordViaEmailToken
from core.services.jwt_service import JWTService

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.models import UserModel as User

from .serializers import EmailSerializer, PasswordSerializer

UserModel: User = get_user_model()


# Create your views here.

class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        email = self.request.data
        serializer = EmailSerializer(data=email)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        user = get_object_or_404(UserModel, email=email)
        EmailService.reset_password_via_email(user)
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = self.kwargs.get('token')
        user = JWTService.validate_token(token, ResetPasswordViaEmailToken)
        data = self.request.data
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.data.get('password'))
        user.save()
        return Response(status=status.HTTP_200_OK)
