from __future__ import unicode_literals

from django.db import models
from school.models import School


class Classes(models.Model):
    school = models.ForeignKey(School)
    year = models.PositiveSmallIntegerField()
    grade = models.PositiveSmallIntegerField()
    class_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'classes'


class Semester(models.Model):
    classes = models.ForeignKey(Classes)
    semester = models.CharField(max_length=30, db_index=True)

    class Meta:
        db_table = 'semester'
