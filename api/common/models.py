from __future__ import unicode_literals

from django.db import models
from classes.models import Semester


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


class CodeSubject(models.Model):
    korean = models.CharField(max_length=100, default='')
    english = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 'code_subject'

    def __unicode__(self):
        return '<CodeSubject(%d) : %s (%s)>' % (self.pk, self.korean, self.english)


class CodeCategory(models.Model):
    category = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'code_category'


class CodeList(models.Model):
    category = models.ForeignKey(CodeCategory, related_name='code_list')
    parent = models.ForeignKey('self', null=True, related_name='parent_code')
    code = models.CharField(max_length=5, db_index=True)
    name = models.CharField(max_length=50)
    is_enabled = models.BooleanField(default=True)

    class Meta:
        db_table = 'code_list'
        unique_together = ('category', 'parent', 'code')


class Tags(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    class Meta:
        db_table = 'tags'
