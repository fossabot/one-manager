from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from onemanager.classes.models import Classes, Semester
from onemanager.student.serializers import StudentSerializer


class SchoolSerializer(ModelSerializer):
    classes = ClassesSerializer(many=True, read_only=True)

    class Meta:
        model = School


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester


class ClassesSerializer(serializers.ModelSerializer):
    semesters = SemesterSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classes
