# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    homepage = models.URLField()

    class Meta:
        db_table = 'school'

    def __unicode__(self):
        return '<School - Name : %s>' % self.name
