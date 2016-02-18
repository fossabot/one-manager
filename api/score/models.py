from __future__ import unicode_literals

from django.db import models
from student.models import Student
from classes.models import Classes, Semester
from common.models import CodeSubjectTemplate


class Score(models.Model):
    classes = models.ForeignKey(Classes)
    semester = models.ForeignKey(Semester)

    class Meta:
        db_table = 'score'


class ScoreData(models.Model):
    score = models.ForeignKey(Score)
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(CodeSubjectTemplate)
    score_data = models.FloatField()

    class Meta:
        db_table = 'score_data'
        unique_together = ('score', 'student',)


class ScoreSummarySubject(models.Model):
    score = models.ForeignKey(Score)
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(CodeSubjectTemplate)
    total = models.FloatField()
    average = models.FloatField()

    class Meta:
        db_table = 'score_summary_subject'
        unique_together = ('score', 'student', 'subject',)


class ScoreSummaryTotal(models.Model):
    score = models.ForeignKey(Score)
    student = models.ForeignKey(Student)
    total = models.FloatField()
    average = models.FloatField()

    class Meta:
        db_table = 'score_summary_total'
        unique_together = ('score', 'student',)
