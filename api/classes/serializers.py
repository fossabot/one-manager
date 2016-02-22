from rest_framework import serializers
from classes.models import Classes, Semester


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ('id', 'school_id', 'teacher_id', 'year', 'grade', 'class_name')
