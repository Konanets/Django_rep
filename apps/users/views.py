from abc import ABC, abstractmethod

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.auto_parks.models import AutoParksModel
from apps.auto_parks.serializers import AutoParkSerializer

from .models import UserModel as User
from .permissions import IsSuperUser
from .serializers import UserSerializer

UserModel: User = get_user_model()


# Create your views here.

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = IsSuperUser,


class AddAutoParkView(GenericAPIView):
    def get(self, *args, **kwargs):
        auto_parks = AutoParksModel.objects.filter(owner_id=self.request.user.pk)
        serializer = AutoParkSerializer(auto_parks, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        user = self.request.user
        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class AdminTools(GenericAPIView, ABC):
    permission_classes = IsAdminUser,

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.id)

    @abstractmethod
    def patch(self, *args, **kwargs):
        pass


class SuperUserTools(AdminTools, ABC):
    permission_classes = IsSuperUser,


class UserActivateView(AdminTools):
    def patch(self, *args, **kwargs):
        user: User = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserDeactivateView(AdminTools):

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToAdmin(SuperUserTools):
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUser(SuperUserTools):

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

