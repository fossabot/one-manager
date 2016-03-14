"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_nested.routers import DefaultRouter, SimpleRouter, NestedSimpleRouter
from auth.views import UserViewSet
from school.views import SchoolViewSet
from classes.views import ClassesViewSet, SemesterViewSet
from students.views import StudentsViewSet

root_router = DefaultRouter()
root_router.register(r'users', UserViewSet)
root_router.register(r'school', SchoolViewSet)
root_router.register(r'classes', ClassesViewSet)
root_router.register(r'semester', SemesterViewSet)
root_router.register(r'student', StudentsViewSet)


school_router = SimpleRouter()
school_router.register('school', SchoolViewSet)
school_classes_router = NestedSimpleRouter(school_router, 'school', lookup='school')
school_classes_router.register('classes', ClassesViewSet, base_name='school-classes')
school_classes_semester_router = NestedSimpleRouter(school_classes_router, 'classes', lookup='classes')
school_classes_semester_router.register('semester', SemesterViewSet, base_name='school-classes-semester')
school_classes_student_router = NestedSimpleRouter(school_classes_router, 'classes', lookup='classes')
school_classes_student_router.register('student', StudentsViewSet, base_name='school-classes-student')

classes_router = SimpleRouter()
classes_router.register('classes', ClassesViewSet)
classes_semester_router = NestedSimpleRouter(classes_router, 'classes', lookup='classes')
classes_semester_router.register('semester', SemesterViewSet, base_name='classes-semester')
classes_student_router = NestedSimpleRouter(classes_router, 'classes', lookup='classes')
classes_student_router.register('student', StudentsViewSet, base_name='classes-student')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/swagger/', include('rest_framework_swagger.urls')),
    url(r'^docs/drf/', include('rest_framework_docs.urls')),
    url(r'^api/', include(root_router.urls)),
    url(r'^api/', include(school_router.urls)),
    url(r'^api/', include(school_classes_router.urls)),
    url(r'^api/', include(school_classes_semester_router.urls)),
    url(r'^api/', include(school_classes_student_router.urls)),
    url(r'^api/', include(classes_router.urls)),
    url(r'^api/', include(classes_semester_router.urls)),
    url(r'^api/', include(classes_student_router.urls)),
]
