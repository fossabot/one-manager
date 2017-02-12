from django.conf.urls import url, include
from rest_framework_nested.routers import SimpleRouter, DefaultRouter, NestedSimpleRouter

from onemanager.api.classes.views import (
    SchoolViewSet, SchoolClassesViewSet, SchoolClassesSemesterViewSet,
    ClassesViewSet, SemesterViewSet, ClassesSemesterViewSet
)
from onemanager.student.views import ClassesStudentViewSet, StudentViewSet

root_router = DefaultRouter()
root_router.register('school', SchoolViewSet, 'school')
root_router.register('classes', ClassesViewSet, 'classes')
root_router.register('semester', SemesterViewSet, 'semester')

classes_router = SimpleRouter()
classes_router.register('classes', ClassesViewSet, base_name='list-classes')
classes_semester_router = NestedSimpleRouter(classes_router, 'classes', lookup='classes')
classes_semester_router.register('semester', ClassesSemesterViewSet, base_name='list-classes-semester')
classes_student_router = NestedSimpleRouter(classes_router, 'classes', lookup='classes')
classes_student_router.register('student', ClassesStudentViewSet, base_name='list-classes-student')

school_router = SimpleRouter()
school_router.register('school', SchoolViewSet, base_name='list-school')
school_classes_router = NestedSimpleRouter(school_router, 'school', lookup='school')
school_classes_router.register('classes', SchoolClassesViewSet, base_name='list-school-classes')
school_classes_semester_router = NestedSimpleRouter(school_classes_router, 'classes', lookup='classes')
school_classes_semester_router.register('semester', SchoolClassesSemesterViewSet,
                                        base_name='list-school-classes-semester')
school_classes_student_router = NestedSimpleRouter(school_classes_router, 'classes', lookup='classes')
school_classes_student_router.register('student', StudentViewSet, base_name='list-school-classes-student')


urlpatterns = [
    url(r'', include(root_router.urls)),
    url(r'list/', include(classes_router.urls)),
    url(r'list/', include(classes_semester_router.urls)),
    url(r'list/', include(classes_student_router.urls)),
    url(r'list/', include(school_router.urls)),
    url(r'list/', include(school_classes_router.urls)),
    url(r'list/', include(school_classes_semester_router.urls)),
    url(r'list/', include(school_classes_student_router.urls)),
]
