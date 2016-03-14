from rest_framework import viewsets
from students.models import Students
from students.serializers import StudentsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
