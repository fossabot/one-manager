from django.conf.urls import url, include
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from classes.views import ClassesViewSet, SemesterViewSet
from classes.views import ClassesSemesterViewSet
from student.views import StudentViewSet
from student.views import ClassesStudentViewSet

classes_router = SimpleRouter()
classes_router.register('classes', ClassesViewSet)
classes_semester_router = NestedSimpleRouter(classes_router, 'classes', lookup='classes')
classes_semester_router.register('semester', ClassesSemesterViewSet, base_name='classes-semester')
classes_student_router = NestedSimpleRouter(classes_router, 'classes', lookup='classes')
classes_student_router.register('student', ClassesStudentViewSet, base_name='classes-student')

urlpatterns = [
    url(r'list/', include(classes_router.urls)),
    url(r'list/', include(classes_semester_router.urls)),
    url(r'list/', include(classes_student_router.urls)),
]
