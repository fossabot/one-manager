from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    GENDER_CHOISES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    student_id = models.AutoField(primary_key=True)
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES, default='M')


class StudentParents(models.Model):
    parent_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=True, related_name='student_parents')
    name = models.CharField(max_length=50)
