from django.shortcuts import render
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .serializers import UserSerializer, PasswordResetSerializer, EmailSerializer

# Create your views here.
class RegisterView(APIView):
    """
    API view for User-Registration.
    validates and creates new user account, if user (email-adress) does not already exists
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if User.objects.filter(email=request.data["email"]).exists():
            return Response({"error": "Email already exists"})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data})


class LoginView(ObtainAuthToken):
    """
    API View for User-Login. 
    provides token-based authentication: login, validating, returning auth-token with userdetails
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class PasswortResetUrlView(generics.GenericAPIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                'reset_password',
                kwargs={'encoded_pk': encoded_pk, 'token': token}
            )
            reset_url = f'localhost:8000{reset_url}'

            return Response(
                { 'message': f'Your passwort reset link: {reset_url}'},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {'message': 'User does not exist'},
                status = status.HTTP_400_BAD_REQUEST,
            )


class PasswordResetView(generics.GenericAPIView):
    def patch(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data, context={'kwargs': kwargs})
        serializer.is_valid(raise_exception=True)

        return Response(
            {'message': 'Password reset complete'},
            status=status.HTTP_200_OK
        )

