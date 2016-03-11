from rest_framework import viewsets
from rest_framework.decorators import detail_route
from students.models import Students
from students.serializers import StudentsSerializer
from rest_framework.response import Response


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
