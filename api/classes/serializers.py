from rest_framework import serializers
from classes.models import Classes, Semesters
from students.serializers import StudentsSerializer


class SemestersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semesters


class ClassesSerializer(serializers.ModelSerializer):
    semesters = SemestersSerializer(many=True, read_only=True)
    students = StudentsSerializer(many=True, read_only=True)

    class Meta:
        model = Classes
