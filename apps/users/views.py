from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParksModel
from apps.auto_parks.serializers import AutoParkSerializer

from .models import UserModel
from .permissions import IsStaff, IsSuperUser
from .serializers import UserSerializer

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


class MakeActiveView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = IsStaff,

    def patch(self, *args, **kwargs):
        user = self.get_object()
        user.is_active = not user.is_active
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class MakeAdminView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = IsSuperUser,

    def patch(self, *args, **kwargs):
        user = self.get_object()
        user.is_staff = not user.is_staff
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
