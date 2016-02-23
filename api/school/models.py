from __future__ import unicode_literals

from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    homepage = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'school'
