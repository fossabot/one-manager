from rest_framework import viewsets
from score.models import Score, ScoreData
from score.serializers import ScoreSerializer, ScoreDataSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class ScoreDataViewSet(viewsets.ModelViewSet):
    queryset = ScoreData.objects.all()
    serializer_class = ScoreDataSerializer
