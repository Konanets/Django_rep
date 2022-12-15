from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer

from .filters import AutoParkFilter
from .models import AutoParksModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = AllowAny,


class AddCarToAutoParkView(GenericAPIView):
    queryset = AutoParksModel.objects.all()
    filterset_class = AutoParkFilter

    def get_permissions(self):
        if self.request.method == 'GET':
            return AllowAny(),
        return IsAuthenticated(),

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        cars = CarModel.objects.filter(auto_park_id=pk)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        serializer = AutoParkSerializer(auto_park)
        return Response(serializer.data, status.HTTP_200_OK)
