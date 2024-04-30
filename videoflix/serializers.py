from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    creats and retrievs user instances
    """
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False,
        )
        
        return user
    
    class Meta:
        model = User
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    # email = serializers.EmailField()

    class Meta:
        model = User
        fields = '_all_'


# class PasswordResetSerializer(serializers.Serializer):
#     password = serializers.CharField(
#         write_only=True,
#         min_length=8,
#     )

#     class Meta:
#         fields = ('password')
    
#     def validate(self, data):
#         password = data.get('password')
#         token = self.context.get('kwargs').get('token')
#         encoded_pk = self.context.get('kwargs').get('encoded_pk')

#         if token is None or encoded_pk is None:
#             raise serializers.ValidationError('Missing data')
        
#         pk = urlsafe_base64_decode(encoded_pk).decode()
#         user = User.objects.get(pk=pk)

#         if not PasswordResetTokenGenerator().check_token(user, token):
#             raise serializers.ValidationError('the reset token is invalid')
        
#         user.set_password(password)
#         user.save()
#         return data


class ActivateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
