from __future__ import unicode_literals

from django.db import models

from onemanager.shared.models import Tags
from onemanager.student.models import Student


class Attendance(models.Model):
    date = models.DateField()
    reason = models.TextField()
    tags = models.ManyToManyField(Tags)

    class Meta:
        abstract = True


class AttendanceLate(Attendance):
    student = models.ForeignKey(Student, related_name='attendance_late')

    class Meta:
        db_table = 'attendance_late'


class AttendanceAbsence(Attendance):
    student = models.ForeignKey(Student, related_name='attendance_absence')

    class Meta:
        db_table = 'attendance_absence'


class AttendanceEarlyLeave(Attendance):
    student = models.ForeignKey(Student, related_name='attendance_early_leave')

    class Meta:
        db_table = 'attendance_early_leave'
