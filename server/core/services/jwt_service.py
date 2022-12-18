from typing import Type

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from apps.users.models import UserModel as User

from ..enums.action_enum import ActionEnum
from ..exceptions.jwt_excep import JwtException

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

TokenClass = Type[BlacklistMixin | Token]
UserModel: User = get_user_model()


class ActivateToken(BlacklistMixin, Token):
    lifetime = ActionEnum.ACTIVATE.ext_time
    token_type = ActionEnum.ACTIVATE.token_type


class ResetPasswordViaEmailToken(BlacklistMixin, Token):
    lifetime = ActionEnum.RESET.ext_time
    token_type = ActionEnum.RESET.token_type


class JWTService:
    @staticmethod
    def create_token(user, token_class: TokenClass):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: TokenClass):
        try:
            valid_token = token_class(token)
            valid_token.check_blacklist()
        except(Exception,):
            raise JwtException
        valid_token.blacklist()
        user_id = valid_token.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
