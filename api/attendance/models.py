from __future__ import unicode_literals

from django.db import models
from student.models import Student
from common.models import Tags


class Attendance(models.Model):
    student = models.ForeignKey(Student)
    date = models.DateField()
    reason = models.TextField()
    tags = models.ManyToManyField(Tags)

    class Meta:
        abstract = True


class AttendanceLate(Attendance):
    class Meta:
        db_table = 'attendance_late'


class AttendanceAbsence(Attendance):
    class Meta:
        db_table = 'attendance_absence'


class AttendanceEarlyLeave(Attendance):
    class Meta:
        db_table = 'attendance_early_leave'
