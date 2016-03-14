from rest_framework import viewsets
from classes.models import Classes, Semesters
from classes.serializers import ClassesSerializer, SemestersSerializer


class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semesters.objects.all()
    serializer_class = SemestersSerializer
