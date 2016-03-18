from rest_framework import viewsets
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from classes.models import Classes, Semester
from classes.serializers import ClassesSerializer, SemesterSerializer


class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class ClassesSemesterViewSet(viewsets.ViewSet):
    serializer_class = SemesterSerializer

    def list(self, request, classes_pk=None):
        queryset = Semester.objects.filter(classes=classes_pk)
        serializer = SemesterSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, classes_pk=None):
        queryset = Semester.objects.filter(classes=classes_pk)
        semester = get_object_or_404(queryset, pk=pk)
        serializer = SemesterSerializer(semester)
        return Response(serializer.data)
