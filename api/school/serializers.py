from school.models import School
from classes.serializers import ClassesSerializer
from rest_framework.serializers import ModelSerializer


class SchoolSerializer(ModelSerializer):
    classes = ClassesSerializer(many=True, read_only=True)

    class Meta:
        model = School
