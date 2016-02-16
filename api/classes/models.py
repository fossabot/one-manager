from __future__ import unicode_literals

from django.db import models


class Classes(models.Model):
    classes_id = models.AutoField(primary_key=True)
    year = models.DecimalField(max_digits=4, null=False)
    grade = models.PositiveSmallIntegerField(default=1)
    semester = models.PositiveSmallIntegerField(default=1)
