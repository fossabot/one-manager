from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from school.models import School
from school.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
