from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class OneManagerUserManager(BaseUserManager):
    def create_user(self, email, password, is_teacher, is_student, is_parent):
        if not email or not password:
            raise ValueError('Users must have an email or password')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.is_teacher = is_teacher
        user.is_student = is_student
        user.is_parent = is_parent

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        if not email or not password:
            raise ValueError('Users must have an email or password')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.is_teacher = True
        user.is_student = True
        user.is_parent = True
        user.is_admin = True

        user.set_password(password)
        user.save(using=self._db)

        return user


class OneManagerUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

    objects = OneManagerUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
