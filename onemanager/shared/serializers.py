from rest_framework import serializers

from onemanager.shared.models import CodeSubject


class CodeSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSubject
