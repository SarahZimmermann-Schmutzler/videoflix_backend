from rest_framework import serializers
from django.contrib.auth.models import User
from videoflix.models import Video

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
    """
    Serializer for the ForgottenPasswordView.
    """
    class Meta:
        model = User
        fields = '_all_'


class ActivateAccountSerializer(serializers.ModelSerializer):
    """
    Serializer for the ActivateAccountView.
    """
    class Meta:
        model = User
        fields = '__all__'


class ResetPasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for the ResetPasswordView.
    """
    class Meta:
        model = User
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for the VideoView.
    """
    class Meta:
        model = Video
        fields = '__all__'