from __future__ import unicode_literals

from django.db import models
from students.models import Students
from classes.models import Classes, Semesters
from common.models import CodeSubjectTemplate


class Score(models.Model):
    classes = models.ForeignKey(Classes, related_name='score')
    semester = models.ForeignKey(Semesters, related_name='score')

    class Meta:
        db_table = 'score'


class ScoreData(models.Model):
    score = models.ForeignKey(Score, related_name='score_data')
    student = models.ForeignKey(Students, related_name='score_data')
    subject = models.ForeignKey(CodeSubjectTemplate, related_name='score_data')
    score_data = models.FloatField()

    class Meta:
        db_table = 'score_data'
        unique_together = ('score', 'student',)


class ScoreSummarySubject(models.Model):
    score = models.ForeignKey(Score, related_name='score_summary_subject')
    student = models.ForeignKey(Students, related_name='score_summary_subject')
    subject = models.ForeignKey(CodeSubjectTemplate, related_name='score_summary_subject')
    total = models.FloatField()
    average = models.FloatField()

    class Meta:
        db_table = 'score_summary_subject'
        unique_together = ('score', 'student', 'subject',)


class ScoreSummaryTotal(models.Model):
    score = models.ForeignKey(Score, related_name='score_summary_total')
    student = models.ForeignKey(Students, related_name='score_summary_total')
    total = models.FloatField()
    average = models.FloatField()

    class Meta:
        db_table = 'score_summary_total'
        unique_together = ('score', 'student',)
