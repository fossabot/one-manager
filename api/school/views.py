from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from school.models import School
from school.serializers import SchoolSerializer
from classes.serializers import ClassesSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @detail_route(methods=['get'])
    def classes(self, request, pk):
        school = self.get_object()
        queryset = school.classes
        instances = self.filter_queryset(queryset)
        serializer = ClassesSerializer(instance=instances, context={'request': request}, many=True)
        return Response(serializer.data)
