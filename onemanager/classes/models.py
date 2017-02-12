from datetime import datetime

from django.conf import settings
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    homepage = models.URLField()
    is_closed = models.BooleanField(default=False)

    class Meta:
        db_table = 'school'

    def __unicode__(self):
        return '{} ({})'.format(self.name, self.pk)


class Classes(models.Model):
    YEAR_CHOICES =[]
    for r in range(datetime.now().year, 1999, -1):
        YEAR_CHOICES.append((r, r))

    school = models.ForeignKey(School, related_name='classes')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='classes')
    year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES, null=False)
    grade = models.CharField(max_length=10, null=False)
    classes = models.CharField(max_length=10, null=False)
    classes_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'classes'
        unique_together = ('school', 'teacher', 'year', 'grade', 'classes')

    def __unicode__(self):
        return '{} ({}, {}-{})'.format(
            self.school.name,
            self.year, self.grade, self.classes
        )


class Semester(models.Model):
    classes = models.ForeignKey(Classes, related_name='semesters')
    semester = models.CharField(max_length=30, db_index=True)

    class Meta:
        db_table = 'semester'
        unique_together = ('classes', 'semester')

    def __unicode__(self):
        return '{} ({}, {}-{}-{})'.format(
            self.school.name,
            self.classes.year, self.classes.grade, self.classes.classes,
            self.semester
        )
