from __future__ import unicode_literals

from django.db import models
from classes.models import Classes, Semesters


class Students(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    STATUS_CHOICES = (
        ('N', 'Normal'),
        ('T', 'Transfer'),
    )

    classes = models.ForeignKey(Classes, related_name='students')
    number = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')

    class Meta:
        db_table = 'students'


class StudentsProfile(models.Model):
    student = models.ForeignKey(Students, related_name='profile')
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    uniqueness = models.TextField()

    class Meta:
        db_table = 'students_profile'


class StudentsFamilies(models.Model):
    RELATIONSHIP_CHOICES = (
        ('F', 'Father'),
        ('M', 'Mother'),
        ('B', 'Brother'),
        ('S', 'Sister'),
        ('GF', 'Grand Father'),
        ('GM', 'Grand Mother'),
    )

    student = models.ForeignKey(Students, related_name='families')
    relationship = models.CharField(max_length=1, choices=RELATIONSHIP_CHOICES)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'students_families'


class StudentsFamiliesProfile(models.Model):
    student_families = models.ForeignKey(StudentsFamilies, related_name='profile')
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    uniqueness = models.TextField()

    class Meta:
        db_table = 'students_families_profile'


class StudentsHistory(models.Model):
    student = models.ForeignKey(Students, related_name='history')
    description = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'students_history'
