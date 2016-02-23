from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from school.models import School
from school.serializers import SchoolSerializer


class SchoolList(APIView):
    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        school = School.objects.all()
        serializer = SchoolSerializer(school, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requst, pk, format=None):
        school = self.get_object(pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SchoolDetail(APIView):
    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requst, pk, format=None):
        school = self.get_object(pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
