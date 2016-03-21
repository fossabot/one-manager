from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from common.models import ContactBase
from classes.models import Classes, Semester


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    STATUS_CHOICES = (
        ('N', 'Normal'),
        ('T', 'Transferred'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=None)
    classes = models.ForeignKey(Classes, related_name='student')
    number = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')

    class Meta:
        db_table = 'student'
        ordering = ('number',)

    def __unicode__(self):
        return '<Student(%d) : Class - %s, Name - %s>' % (self.pk, self.classes.classes_name, self.name)


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

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=None)
    student = models.ForeignKey(Student, related_name='family')
    relationship = models.CharField(max_length=2, choices=RELATIONSHIP_CHOICES)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'student_family'


class StudentFamilyProfile(models.Model):
    family = models.ForeignKey(StudentFamily, related_name='profile')
    address = models.CharField(max_length=255)
    uniqueness = models.TextField()

    class Meta:
        db_table = 'student_family_profile'


class StudentFamilyContact(ContactBase):
    family = models.ForeignKey(StudentFamily, related_name='contact')

    class Meta:
        db_table = 'student_family_contact'


class StudentHistory(models.Model):
    student = models.ForeignKey(Student, related_name='history')
    description = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_history'
