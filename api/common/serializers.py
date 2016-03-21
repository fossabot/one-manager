from rest_framework import serializers
from common.models import CodeSubject


class CodeSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSubject
