from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    """
    Custom User model for authentication, replacing the username field with email.
    
    This model extends :model:`auth.AbstractUser`, removes the default `username` field,
    and uses the `email` field as the unique identifier for authentication. It also adds
    a `phone` field and a method `full_name()` to return the user's full name if available.
    
    **Attributes:**
        email (str): The email address, used as the unique identifier for login and authentication.
        phone (str): The user's phone number, optional.
        
    **Meta:**
        `USERNAME_FIELD`: Specifies that `email` is the unique identifier for authentication.
        `REQUIRED_FIELDS`: An empty list as we don't require any additional fields for user creation.
    
    **Methods:**
        __str__(): Returns the user's email as a string representation.
        full_name(): Returns the user's full name if both `first_name` and `last_name` are set, else returns the email.
    
    **Managers:**
        objects: The custom UserManager to handle user creation logic.
    """
    # remove the username field
    username = None
    
    # set email field with the unique constraint
    email = models.EmailField(_("email address"), unique=True)

    # set the email field as the unique identifier instead of username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=20, blank=True)

    # set the relationship to the custom UserManager
    objects = UserManager()

    def __str__(self):
        """
        Returns the user's email address as a string.

        Returns:
            str: The email address of the user.
        """
        return self.email
    
    def full_name(self):
        """
        Returns the full name of the user by combining the first and last names, 
        if both are provided. If either is missing, returns the email address.

        Returns:
            str: The full name of the user, or the email if full name is unavailable.
        """
        if self.first_name != "" and self.last_name != "":
            return f"{self.first_name} {self.last_name}"
        else:
            return self.__str__()
