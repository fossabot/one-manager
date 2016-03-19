# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.conf import settings
from django.db import models
from school.models import School


class Classes(models.Model):
    YEAR_CHOICES =[]
    for r in range(datetime.now().year, 1999, -1):
        YEAR_CHOICES.append((r, r))

    school = models.ForeignKey(School, related_name='classes')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='classes')
    year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES, default=datetime.now().year, null=False)
    grade = models.CharField(max_length=10, null=False)
    classes = models.CharField(max_length=10, null=False)
    classes_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'classes'
        unique_together = ('school', 'teacher', 'year', 'grade', 'classes')

    def __str__(self):
        return '<Classes - %s학교 %d년 %s학년 %s반 (%s)>' % (
            self.school.name,
            self.year,
            self.grade,
            self.classes,
            self.classes_name
        )


class Semester(models.Model):
    classes = models.ForeignKey(Classes, related_name='semesters')
    semester = models.CharField(max_length=30, db_index=True)

    class Meta:
        db_table = 'semester'
        unique_together = ('classes', 'semester')

    def __str__(self):
        return '<Semester - %s학교 %d년 %s학년 %s반 (%s) %s학기>' % (
            self.classes.school.name,
            self.classes.year,
            self.classes.grade,
            self.classes.classes,
            self.classes.classes_name,
            self.semester
        )
