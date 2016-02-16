from __future__ import unicode_literals

from django.db import models


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    homepage = models.CharField(max_length=255)
