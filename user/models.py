from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    cpf = models.CharField(_("CPF"), max_length=14, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-date_joined"]
