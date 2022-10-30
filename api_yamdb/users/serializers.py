from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name',
                  'last_name',
                  'username',
                  'bio',
                  'email',
                  'role'
                  )
        read_only_fields = ('role', 'email')
        model = User


class UserForAdminSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name',
                  'last_name',
                  'username',
                  'bio',
                  'email',
                  'role'
                  )
        model = User


class CheckConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
