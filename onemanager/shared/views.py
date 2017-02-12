from common.serializers import CodeSubjectSerializer
from rest_framework import viewsets

from onemanager.shared.models import CodeSubject


class CodeSubjectViewSet(viewsets.ModelViewSet):
    queryset = CodeSubject.objects.all()
    serializer_class = CodeSubjectSerializer
