from __future__ import unicode_literals

from django.db import models
from classes.models import Classes, Semester


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    STATUS_CHOICES = (
        ('N', 'Normal'),
        ('T', 'Transfer'),
    )

    classes = models.ForeignKey(Classes, related_name='students')
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')

    class Meta:
        db_table = 'student'


class StudentProfile(models.Model):
    student = models.ForeignKey(Student, related_name='profile')
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    uniqueness = models.TextField()

    class Meta:
        db_table = 'student_profile'


class StudentFamilies(models.Model):
    RELATIONSHIP_CHOICES = (
        ('F', 'Father'),
        ('M', 'Mother'),
        ('B', 'Brother'),
        ('S', 'Sister'),
        ('GF', 'Grand Father'),
        ('GM', 'Grand Mother'),
    )

    student = models.ForeignKey(Student, related_name='families')
    relationship = models.CharField(max_length=1, choices=RELATIONSHIP_CHOICES)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'student_families'


class StudentFamiliesProfile(models.Model):
    student_families = models.ForeignKey(StudentFamilies, related_name='profile')
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    uniqueness = models.TextField()

    class Meta:
        db_table = 'student_families_profile'


class StudentHistory(models.Model):
    student = models.ForeignKey(Student, related_name='history')
    description = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_history'
