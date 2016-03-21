from rest_framework import serializers
from score.models import Score, ScoreData


class ScoreDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreData


class ScoreSerializer(serializers.ModelSerializer):
    score_data = ScoreDataSerializer(many=True, read_only=True)

    class Meta:
        model = Score
