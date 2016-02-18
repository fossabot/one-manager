from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.school.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = SchoolSerializer
