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
from rest_framework.routers import DefaultRouter
from auth.views import UserViewSet
from school.views import SchoolViewSet
from classes.views import ClassesViewSet, SemesterViewSet
from students.views import StudentsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'school', SchoolViewSet)
router.register(r'classes', ClassesViewSet)
router.register(r'semester', SemesterViewSet)
router.register(r'students', StudentsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/swagger/', include('rest_framework_swagger.urls')),
    url(r'^docs/drf/', include('rest_framework_docs.urls')),
    url(r'^api/', include(router.urls)),
]

"""
/school - School list / create
/shcool/pk - School detail / update / delete
/school/pk/classes - Classes list in school's pk
/classes - Classes list / create
/classes/pk - Classes detail / update / delete
/classes/pk/semester - Semester list in classes's pk
/semester - Semester list / create
/semester/pk - Semester detail / update / delete
/semester/pk/students - Student list in semester's pk
/students - Student
"""