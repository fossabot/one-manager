from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from classes.models import Classes, Semester


class ContactBase(models.Model):
    CONTACT_TYPE = (
        ('H', 'Home'),
        ('M', 'Mobile'),
        ('O', 'Other'),
        ('E', 'Email'),
    )

    contact_type = models.CharField(max_length=2, choices=CONTACT_TYPE, null=False)
    contact = models.CharField(max_length=50, null=False)

    class Meta:
        abstract = True


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    STATUS_CHOICES = (
        ('N', 'Normal'),
        ('T', 'Transferred'),
    )

    user = models.ForeignKey(User, null=True, default=None)
    classes = models.ForeignKey(Classes, related_name='student')
    number = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')

    class Meta:
        db_table = 'student'
        ordering = ('number',)


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, related_name='profile')
    address = models.CharField(max_length=255)
    uniqueness = models.TextField()

    class Meta:
        db_table = 'student_profile'


class StudentContact(ContactBase):
    student = models.ForeignKey(Student, related_name='contact')

    class Meta:
        db_table = 'student_contact'


class StudentFamily(models.Model):
    RELATIONSHIP_CHOICES = (
        ('F', 'Father'),
        ('M', 'Mother'),
        ('B', 'Brother'),
        ('S', 'Sister'),
        ('GF', 'Grand Father'),
        ('GM', 'Grand Mother'),
        ('E', 'ETC'),
    )

    user = models.ForeignKey(User, null=True, default=None)
    student = models.ForeignKey(Student, related_name='family')
    relationship = models.CharField(max_length=2, choices=RELATIONSHIP_CHOICES)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'student_family'


class StudentFamilyProfile(models.Model):
    student_family = models.ForeignKey(StudentFamily, related_name='profile')
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    uniqueness = models.TextField()

    class Meta:
        db_table = 'student_family_profile'


class StudentFamilyContact(ContactBase):
    student = models.ForeignKey(StudentFamily, related_name='contact')

    class Meta:
        db_table = 'student_family_contact'


class StudentHistory(models.Model):
    student = models.ForeignKey(Student, related_name='history')
    description = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_history'
