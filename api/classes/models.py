from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from school.models import School


class Classes(models.Model):
    YEAR_CHOICES =[]
    for r in xrange(datetime.now().year, 1999, -1):
        YEAR_CHOICES.append((r, r))

    school = models.ForeignKey(School, related_name='classes')
    teacher = models.ForeignKey(User, related_name='classes')
    year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES, default=datetime.now().year, null=False)
    grade = models.CharField(max_length=10, null=False)
    class_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'classes'
        unique_together = ('school', 'teacher', 'year', 'grade', 'class_name')

    def __str__(self):
        return 'School : %s, Year : %d, Grade : %s, Class : %s' % (self.school.name,
                                                                   self.year,
                                                                   self.grade,
                                                                   self.class_name)


class Semesters(models.Model):
    classes = models.ForeignKey(Classes, related_name='semesters')
    semester = models.CharField(max_length=30, db_index=True)

    class Meta:
        db_table = 'semesters'
        unique_together = ('classes', 'semester')

    def __str__(self):
        return self.semester
