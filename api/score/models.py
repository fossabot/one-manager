from __future__ import unicode_literals

from django.db import models
from student.models import Student
from classes.models import Classes, Semester
from common.models import CodeSubject


class Score(models.Model):
    classes = models.ForeignKey(Classes, related_name='score')
    semester = models.ForeignKey(Semester, related_name='score')
    term = models.CharField(max_length=10)

    class Meta:
        db_table = 'score'
        unique_together = ('classes', 'semester', 'term')

    def __unicode__(self):
        return '<Score(%d) : Class - %s, Semester - %s, Term - %s>' % (
            self.pk,
            self.classes.classes_name,
            self.semester.semester,
            self.term
        )


class ScoreData(models.Model):
    score = models.ForeignKey(Score, related_name='score_data')
    student = models.ForeignKey(Student, related_name='score_data')
    subject = models.ForeignKey(CodeSubject)
    score_data = models.FloatField()

    class Meta:
        db_table = 'score_data'
        unique_together = ('score', 'student', 'subject')
