from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    @staticmethod
    def _validate_email(email):
        if email and '@' in email:
            return True

    def create_user(self, email, password, **extra_fields):
        """ Creates and saves a new user """
        if not self._validate_email(email):
            raise ValueError('Email is incorrect or empty.')

        if not password:
            raise ValueError('Password is empty.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(raw_password=password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports using email instead of username """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
