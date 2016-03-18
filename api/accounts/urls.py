from django.conf.urls import url, include
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from accounts.views import UserViewSet, UserProfileViewSet, UserContactViewSet


user_router = SimpleRouter()
user_router.register('user', UserViewSet, base_name='user')
user_profile_router = NestedSimpleRouter(user_router, 'user', lookup='user')
user_profile_router.register('profile', UserProfileViewSet, base_name='user-profile')
user_contact_router = NestedSimpleRouter(user_router, 'user', lookup='user')
user_contact_router.register('contact', UserContactViewSet, base_name='user-contact')

urlpatterns = [
    url(r'', include(user_router.urls)),
    url(r'', include(user_profile_router.urls)),
    url(r'', include(user_contact_router.urls)),
]
