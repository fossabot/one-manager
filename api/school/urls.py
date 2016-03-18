from django.conf.urls import url, include
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from school.views import SchoolViewSet
from classes.views import ClassesViewSet, SemesterViewSet
from school.views import SchoolViewSet, SchoolClassesViewSet, SchoolClassesSemesterViewSet
from student.views import StudentViewSet

root_router = SimpleRouter()
root_router.register('school', SchoolViewSet, 'school')

school_router = SimpleRouter()
school_router.register('school', SchoolViewSet)
school_classes_router = NestedSimpleRouter(school_router, 'school', lookup='school')
school_classes_router.register('classes', SchoolClassesViewSet, base_name='school-classes')
school_classes_semester_router = NestedSimpleRouter(school_classes_router, 'classes', lookup='classes')
school_classes_semester_router.register('semester', SchoolClassesSemesterViewSet, base_name='school-classes-semester')
school_classes_student_router = NestedSimpleRouter(school_classes_router, 'classes', lookup='classes')
school_classes_student_router.register('student', StudentViewSet, base_name='school-classes-student')

urlpatterns = [
    url(r'', include(root_router.urls)),
    url(r'list/', include(school_router.urls)),
    url(r'list/', include(school_classes_router.urls)),
    url(r'list/', include(school_classes_semester_router.urls)),
    url(r'list/', include(school_classes_student_router.urls)),
]
