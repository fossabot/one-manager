from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from classes.models import Classes, Semester
from classes.serializers import ClassesSerializer, SemesterSerializer


class ClassesList(APIView):
    def get_object(self, pk):
        try:
            return Classes.objects.get(pk)
        except Classes.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requst, pk, format=None):
        classes = self.get_object(pk)
        classes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassesDetail(APIView):
    def get_object(self, pk):
        try:
            return Classes.objects.get(pk=pk)
        except Classes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        classes = self.get_object(pk)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        classes = self.get_object(pk)
        serializer = ClassesSerializer(classes, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requst, pk, format=None):
        classes = self.get_object(pk)
        classes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SemesterList(APIView):
    def get_object(self, pk):
        try:
            return Semester.objects.get(pk=pk)
        except Classes.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        semester = Semester.objects.all()
        serializer = SemesterSerializer(semester, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SemesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requst, pk, format=None):
        classes = self.get_object(pk)
        classes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
