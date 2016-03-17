from rest_framework import viewsets
from classes.models import Classes, Semester
from classes.serializers import ClassesSerializer, SemesterSerializer


class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
