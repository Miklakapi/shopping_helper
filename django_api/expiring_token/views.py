from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework.views import APIView

from .authentication import is_token_expired, token_expire_handler
from .models import ExpiringToken
from .serializers import UserSigninSerializer
from .serializers import TokenSerializer


class LoginView(APIView):
    serializer_class = UserSigninSerializer
    permission_classes = []

    def post(self, request):
        signin_serializer = UserSigninSerializer(data=request.data)
        if not signin_serializer.is_valid():
            return Response(signin_serializer.errors, status=HTTP_400_BAD_REQUEST)

        user = authenticate(
            username=signin_serializer.data['username'],
            password=signin_serializer.data['password']
        )

        if not user:
            return Response({'detail': 'Invalid Credentials'}, status=HTTP_400_BAD_REQUEST)

        token, _ = ExpiringToken.objects.get_or_create(user=user)

        is_expired, token = token_expire_handler(token)

        return Response(
            {
                'token': token.key,
                'expires': token.expires,
                'username': token.user.username
            },
            status=HTTP_200_OK
        )


class isLoginView(APIView):
    serializer_class = TokenSerializer

    def post(self, request):
        token_serializer = TokenSerializer(data=request.data)
        if not token_serializer.is_valid():
            return Response(token_serializer.errors, status=HTTP_400_BAD_REQUEST)

        token = ExpiringToken.objects.get(key=token_serializer.data['key'])
        if is_token_expired(token):
            return Response(status=HTTP_403_FORBIDDEN)

        return Response(
            {
                'token': token.key,
                'expires': token.expires,
                'username': token.user.username
            },
            status=HTTP_200_OK
        )
