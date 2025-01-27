from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """
    A custom User model to utilise Django's authentication
    but remove the username field
    """
    # remove the username field
    username = None
    
    # set email field with the unique constraint
    email = models.EmailField(_("email address"), unique=True)

    # set the email field as the unique identifier instead of username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # set the relationship to the custom UserManager
    objects = UserManager()

    def __str__(self):
        return self.email
