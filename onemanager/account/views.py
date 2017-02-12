from account.models import OneManagerUser as User, OneManagerUserProfile as UserProfile,\
    OneManagerUserContact as UserContact
from rest_framework.viewsets import ModelViewSet

from onemanager.account.serializers import UserSerializer, UserProfileSerializer, UserContactSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserContactViewSet(ModelViewSet):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer
