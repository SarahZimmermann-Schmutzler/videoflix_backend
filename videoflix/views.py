from django.shortcuts import render
from django.urls import reverse
import os, ssl, smtplib
from email.message import EmailMessage
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .serializers import EmailSerializer, ResetPasswordSerializer, UserSerializer, ActivateAccountSerializer

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


# class PasswortResetUrlView(generics.GenericAPIView):
#     def post(self, request):
#         serializer = EmailSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.data['email']
#         user = User.objects.filter(email=email).first()
#         if user:
#             encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
#             token = PasswordResetTokenGenerator().make_token(user)
#             reset_url = reverse(
#                 'reset_password',
#                 kwargs={'encoded_pk': encoded_pk, 'token': token}
#             )
#             reset_url = f'localhost:8000{reset_url}'

#             return Response(
#                 { 'message': f'Your passwort reset link: {reset_url}'},
#                 status=status.HTTP_200_OK,
#             )
#         else:
#             return Response(
#                 {'message': 'User does not exist'},
#                 status = status.HTTP_400_BAD_REQUEST,
#             )


# class PasswordResetView(generics.GenericAPIView):
#     def patch(self, request, *args, **kwargs):
#         serializer = PasswordResetSerializer(data=request.data, context={'kwargs': kwargs})
#         serializer.is_valid(raise_exception=True)

#         return Response(
#             {'message': 'Password reset complete'},
#             status=status.HTTP_200_OK
#         )

# def activation(request, **kwargs):
#     if request.method == 'GET':
#         return render(request, 'activation.html')
    

class ActivateNewAccountView(APIView):
    def patch(self, request,):
        decoded_pk = request.data.get('decoded_pk')
        user = User.objects.get(pk=decoded_pk)
        user.is_active = True
        serializer=ActivateAccountSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class ForgottenPasswordView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk= urlsafe_base64_encode(force_bytes(user.pk))
            activation_url = f'localhost:4200/resetPassword/{encoded_pk}'
            # send mail with link to new user
            email_sender='sarah.zimmermannschmutzler@gmail.com'
            email_password=os.environ.get("GMAIL_PWD")
            email_receiver=user.email
            subject='VIDEOFLIX Team'
            body=f'Hi {user.username}, here is your Link to reset your VIDEOFLIX password: http://{activation_url}' 

            em=EmailMessage()
            em['From']=email_sender
            em['To']=email_receiver
            em['Subject']=subject
            em.set_content(body)
            context=ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

        return Response(serializer.errors) 


class ResetPasswordView(APIView):
    def patch(self, request):
        decoded_pk = request.data.get('decoded_pk')
        password = request.data.get('new_password')
        user = User.objects.get(pk=decoded_pk)
        user.set_password(password)
        serializer=ResetPasswordSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


