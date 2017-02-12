from django.conf.urls import url, include
from rest_framework_nested.routers import DefaultRouter

from onemanager.student.views import StudentViewSet

root_router = DefaultRouter()
root_router.register('student', StudentViewSet, 'student')

urlpatterns = [
    url(r'', include(root_router.urls)),
]
