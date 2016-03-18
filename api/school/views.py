from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from classes.models import Classes, Semester
from classes.serializers import ClassesSerializer, SemesterSerializer
from school.models import School
from school.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolClassesViewSet(viewsets.ViewSet):
    serializer_class = ClassesSerializer

    def list(self, request, school_pk=None):
        queryset = Classes.objects.filter(school=school_pk)
        serializer = ClassesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, school_pk=None):
        queryset = Classes.objects.filter(school=school_pk)
        classes = get_object_or_404(queryset, pk=pk)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)


class SchoolClassesSemesterViewSet(viewsets.ViewSet):
    serializer_class = SemesterSerializer

    def list(self, request, school_pk=None, classes_pk=None):
        queryset = Semester.objects.filter(classes__school=school_pk, classes=classes_pk)
        serializer = SemesterSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, school_pk=None, classes_pk=None):
        queryset = Semester.objects.filter(classes__school=school_pk, classes=classes_pk)
        semester = get_object_or_404(queryset, pk=pk)
        serializer = SemesterSerializer(semester)
        return Response(serializer.data)
