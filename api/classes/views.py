from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from classes.models import Classes, Semesters
from classes.serializers import ClassesSerializer, SemestersSerializer
from students.serializers import StudentsSerializer
from rest_framework.response import Response


class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

    @detail_route(methods=['get'])
    def semesters(self, request, pk):
        classes = self.get_object()
        queryset = classes.semesters
        instances = self.filter_queryset(queryset)
        serializer = SemestersSerializer(instance=instances, context={'request': request}, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def students(self, request, pk):
        classes = self.get_object()
        queryset = classes.students
        instances = self.filter_queryset(queryset)
        serializer = StudentsSerializer(instance=instances, context={'request': request}, many=True)
        return Response(serializer.data)


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semesters.objects.all()
    serializer_class = SemestersSerializer
