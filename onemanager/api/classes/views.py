from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from onemanager.classes.models import School, Classes, Semester
from onemanager.api.classes.serializers import SchoolSerializer, ClassesSerializer, SemesterSerializer


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
