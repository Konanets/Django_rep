from django.urls import path

from .views import AddCarToAutoParkView, AutoParkListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>/cars', AddCarToAutoParkView.as_view(), name='create_car_in_auto_park'),
]
