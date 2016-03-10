from rest_framework.serializers import ModelSerializer, ModelField
from classes.models import Classes, Semester


class ClassesSerializer(ModelSerializer):
    class Meta:
        model = Classes
        fields = ('id', 'school', 'teacher', 'year', 'grade', 'class_name')


class SemesterSerializer(ModelSerializer):
    class Meta:
        model = Semester
        fields = ('id', 'semester', 'classes')
