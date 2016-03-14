from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class OneManagerUser(AbstractBaseUser):
    MEMBER_TYPE = (
        ('T', 'Teacher'),
        ('S', 'Student'),
        ('P', 'Parent'),
    )

    member_type = models.CharField(max_length=1, choices=MEMBER_TYPE, null=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['member_type', 'email', 'first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
