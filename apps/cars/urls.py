from django.urls import path

from .views import CarListCreateView, CarRetrieveUpdateDestroyView, CarPhotoUpdateView

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>/photo', CarPhotoUpdateView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view()),

]
