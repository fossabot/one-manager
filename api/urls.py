from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_nested.routers import DefaultRouter, SimpleRouter, NestedSimpleRouter, LookupMixin
from accounts.views import UserViewSet, UserProfileViewSet, UserContactViewSet
from school.views import SchoolViewSet
from classes.views import ClassesViewSet, SemesterViewSet
from student.views import StudentViewSet

root_router = DefaultRouter()
root_router.register(r'user', UserViewSet)
root_router.register(r'school', SchoolViewSet)
root_router.register(r'classes', ClassesViewSet)
root_router.register(r'semester', SemesterViewSet)
root_router.register(r'student', StudentViewSet)

user_router = SimpleRouter()
user_router.register('user', UserViewSet, base_name='user')
# user_profile_router = NestedSimpleRouter(user_router, 'user', lookup='user')
# user_profile_router.register('profile', UserProfileViewSet, base_name='user-profile')
user_contact_router = NestedSimpleRouter(user_router, 'user', lookup='user')
user_contact_router.register('contact', UserContactViewSet, base_name='user-contact')

school_router = SimpleRouter()
school_router.register('school', SchoolViewSet)
school_classes_router = NestedSimpleRouter(school_router, 'school', lookup='school')
school_classes_router.register('classes', ClassesViewSet, base_name='school-classes')
school_classes_semester_router = NestedSimpleRouter(school_classes_router, 'classes', lookup='classes')
school_classes_semester_router.register('semester', SemesterViewSet, base_name='school-classes-semester')
school_classes_student_router = NestedSimpleRouter(school_classes_router, 'classes', lookup='classes')
school_classes_student_router.register('student', StudentViewSet, base_name='school-classes-student')

classes_router = SimpleRouter()
classes_router.register('classes', ClassesViewSet)
classes_semester_router = NestedSimpleRouter(classes_router, 'classes', lookup='classes')
classes_semester_router.register('semester', SemesterViewSet, base_name='classes-semester')
classes_student_router = NestedSimpleRouter(classes_router, 'classes', lookup='classes')
classes_student_router.register('student', StudentViewSet, base_name='classes-student')

urlpatterns = [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/swagger/', include('rest_framework_swagger.urls')),
    url(r'^docs/drf/', include('rest_framework_docs.urls')),
    url(r'^api/', include(root_router.urls)),
    url(r'^api/', include(user_router.urls)),
    # url(r'^api/', include(user_profile_router.urls)),
    url(r'^api/', include(user_contact_router.urls)),
    url(r'^api/', include(school_router.urls)),
    url(r'^api/', include(school_classes_router.urls)),
    url(r'^api/', include(school_classes_semester_router.urls)),
    url(r'^api/', include(school_classes_student_router.urls)),
    url(r'^api/', include(classes_router.urls)),
    url(r'^api/', include(classes_semester_router.urls)),
    url(r'^api/', include(classes_student_router.urls)),
]
