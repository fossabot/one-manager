from rest_framework import serializers
from classes.models import Classes, Semester
from student.serializers import StudentSerializer


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester


class ClassesSerializer(serializers.ModelSerializer):
    semesters = SemesterSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classes
