from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users import views
from users.views import UsersViewSet, get_jwt_token

v1_router = DefaultRouter()
v1_router.register(r'users', UsersViewSet, basename='users')

auth_urlpatterns = [

    path('token/', get_jwt_token, name='send_confirmation_code'),
    path(
        'email/',
        views.send_confirmation_code,
        name='send_confirmation_code'
    ),

]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include(auth_urlpatterns))
]
