from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import filters

from api_yamdb import settings
from users.permisions import IsAdmin
from users.serializers import CheckConfirmationCodeSerializer
from users.serializers import (EmailSerializer,
                               UserForAdminSerializer)

User = get_user_model()


@api_view(['POST'])
def send_confirmation_code(request):
    serializer = EmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data['email']
    username = serializer.data['username']
    user = User.objects.get_or_create(email=email,
                                      username=username)[0]
    confirmation_code = default_token_generator.make_token(user)
    mail_subject = 'Код подтверждения на Yamdb.ru'
    message = f'Ваш код подтверждения: {confirmation_code}'
    send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [email])
    return Response(f'Код отправлен на адрес {email}',
                    status=status.HTTP_200_OK)


@api_view(['POST'])
def get_jwt_token(request):
    serializer = CheckConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data['email']
    confirmation_code = serializer.data['confirmation_code']
    user = get_object_or_404(User, email=email)
    if default_token_generator.check_token(user, confirmation_code):
        token = AccessToken.for_user(user)
        return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
    return Response({'confirmation_code': 'Неверный код подтверждения'},
                    status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(ModelViewSet):
    serializer_class = UserForAdminSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = (IsAuthenticated, IsAdmin)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=username',)

    @action(detail=False, permission_classes=(IsAuthenticated,),
            methods=['get', 'patch'])
    def me(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(role=user.role)

        return Response(serializer.data, status=status.HTTP_200_OK)
