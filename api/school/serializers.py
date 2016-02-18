from django.contrib.auth.models import User, Group
from rest_framework import serializers


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'school_id', 'name', 'address', 'homepage')
