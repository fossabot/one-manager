from accounts.models import OneManagerUser as User, OneManagerUserProfile as UserProfile,\
    OneManagerUserContact as UserContact
from rest_framework.serializers import ModelSerializer


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile


class UserContactSerializer(ModelSerializer):
    class Meta:
        model = UserContact


class UserSerializer(ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    contact = UserContactSerializer(many=True, read_only=True)

    class Meta:
        model = User
