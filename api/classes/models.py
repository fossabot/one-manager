from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from school.models import School


class Classes(models.Model):
    school = models.ForeignKey(School, related_name='classes')
    teacher = models.ForeignKey(User, related_name='classes')
    year = models.PositiveSmallIntegerField()
    grade = models.PositiveSmallIntegerField()
    class_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'classes'


class Semester(models.Model):
    classes = models.ForeignKey(Classes, related_name='semester')
    semester = models.CharField(max_length=30, db_index=True)

    class Meta:
        db_table = 'semester'
