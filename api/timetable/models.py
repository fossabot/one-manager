from __future__ import unicode_literals

from django.db import models
from classes.models import Semester


class TimeTable(models.Model):
    DAY_OF_WEEK_CHOICES = (
        ('Sun', 'Sunday'),
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
    )

    semester = models.ForeignKey(Semester, related_name='timetable')
    day_of_week = models.CharField(max_length=3, choices=DAY_OF_WEEK_CHOICES)
    subject = models.CharField(max_length=30)
    period = models.CommaSeparatedIntegerField(max_length=100)

    class Meta:
        db_table = 'time_table'
