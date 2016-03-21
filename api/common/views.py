from rest_framework import viewsets
from common.models import CodeSubject
from common.serializers import CodeSubjectSerializer


class CodeSubjectViewSet(viewsets.ModelViewSet):
    queryset = CodeSubject.objects.all()
    serializer_class = CodeSubjectSerializer
