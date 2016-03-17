from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from common.models import ContactBase


class UserManager(BaseUserManager):
    def create_user(self, email, password, is_teacher, is_student, is_parent, first_name, last_name):
        if not email or not password:
            raise ValueError('Users must have an email or password')

        user = self.model(
            email=self.normalize_email(email),
            is_teacher=is_teacher,
            is_student=is_student,
            is_parent=is_parent
        )

        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name, last_name):
        if not email or not password:
            raise ValueError('Users must have an email or password')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.first_name = first_name
        user.last_name = last_name
        user.is_teacher = True
        user.is_student = True
        user.is_parent = True
        user.is_admin = True

        user.set_password(password)
        user.save(using=self._db)

        return user


class OneManagerUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email Address',
        unique=True
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'login_user'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class OneManagerUserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'login_user_profile'


class OneManagerUserContact(ContactBase):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contact')

    class Meta:
        db_table = 'login_user_contact'
