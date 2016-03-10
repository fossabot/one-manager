from school.models import School
from rest_framework.serializers import ModelSerializer


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'address', 'homepage')
