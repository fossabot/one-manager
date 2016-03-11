from rest_framework import serializers
from classes.models import Classes, Semesters
from school.serializers import SchoolSerializer


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes


class SemestersSerializer(serializers.ModelSerializer):
    school = SchoolSerializer
    classes = ClassesSerializer

    class Meta:
        model = Semesters
