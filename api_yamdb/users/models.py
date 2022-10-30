from django.contrib.auth.models import AbstractUser
from django.db import models


class Roles(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.USER,
    )

    bio = models.TextField(blank=True)

    @property
    def is_admin(self):
        return self.is_staff or self.role == Roles.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == Roles.MODERATOR
