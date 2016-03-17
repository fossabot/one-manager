from rest_framework.viewsets import ModelViewSet
from accounts.models import OneManagerUser as User, OneManagerUserProfile as UserProfile,\
    OneManagerUserContact as UserContact
from accounts.serializers import UserSerializer, UserProfileSerializer, UserContactSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserContactViewSet(ModelViewSet):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer
