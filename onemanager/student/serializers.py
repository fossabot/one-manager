from rest_framework import serializers

from onemanager.student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
