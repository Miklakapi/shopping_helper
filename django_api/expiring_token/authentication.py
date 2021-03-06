import typing
from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import ExpiringToken
from .settings import custom_settings


def expires_in(token: ExpiringToken) -> timedelta:
    time_elapsed = timezone.now() - token.created
    return custom_settings.EXPIRING_TOKEN_DURATION - time_elapsed


def is_token_expired(token: ExpiringToken) -> bool:
    return expires_in(token) < timedelta(seconds=0)


def token_expire_handler(token: ExpiringToken) -> typing.Tuple[bool, ExpiringToken]:
    is_expired = is_token_expired(token)
    if is_expired:
        token.delete()
        token: ExpiringToken = ExpiringToken.objects.create(user=token.user)
    return is_expired, token


class ExpiringTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key: str) -> typing.Tuple[User, ExpiringToken]:
        try:
            token = ExpiringToken.objects.get(key=key)
        except ExpiringToken.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")

        if not token.user.is_active:
            raise AuthenticationFailed("User is not active")

        is_expired, token = token_expire_handler(token)
        if is_expired:
            raise AuthenticationFailed("The Token is expired")

        token.expires = timezone.now() + custom_settings.EXPIRING_TOKEN_DURATION
        token.save()

        return token.user, token
