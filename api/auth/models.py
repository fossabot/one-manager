from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    MEMBER_TYPE = (
        ('t', 'Teacher'),
        ('s', 'Student'),
    )

    user = models.OneToOneField(User)
    member_type = models.CharField(max_length=1, choices=MEMBER_TYPE, null=False)

    class Meta:
        db_table = 'auth_user_profile'
