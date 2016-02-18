from __future__ import unicode_literals

from django.db import models
from classes.models import Semester


class CodeSubject(models.Model):
    code = models.CharField(max_length=10, db_index=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'code_subject'


class CodeSubjectTemplate(models.Model):
    semester = models.ForeignKey(Semester)
    code = models.ForeignKey(CodeSubject)

    class Meta:
        db_table = 'code_subject_template'
        unique_together = ('semester', 'code',)


class Tags(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    class Meta:
        db_table = 'tags'
