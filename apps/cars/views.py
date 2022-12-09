from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import AllowAny

from .models import CarModel, CarsPhotoModel
from .serializers import CarSerializer, CarPhotoSerializer
from rest_framework.response import Response
from rest_framework import status


class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_queryset(self):
        if (auto_park_id := self.request.query_params.dict().get('auto_park_id')) and auto_park_id.isdigit():
            return self.queryset.filter(auto_park_id=auto_park_id)

        return super().get_queryset()


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()


class CarPhotoUpdateView(GenericAPIView):
    queryset = CarModel.objects.all()

    def post(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for key in files:
            serializer = CarPhotoSerializer(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_201_CREATED)
