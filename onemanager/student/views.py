from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from student.serializers import StudentSerializer

from onemanager.student.models import Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ClassesStudentViewSet(viewsets.ViewSet):
    serializer_class = StudentSerializer

    def list(self, request, classes_pk=None):
        queryset = Student.objects.filter(classes=classes_pk)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, classes_pk=None):
        queryset = Student.objects.filter(classes=classes_pk)
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def create(self, request, classes_pk=None):
        pass

    def update(self, request, pk=None, classes_pk=None):
        pass

    def destroy(self, pk=None, classes_pk=None):
        import pdb; pdb.set_trace()
        queryset = Student.objects.filter(pk=pk)
        return Response(queryset.delete())
