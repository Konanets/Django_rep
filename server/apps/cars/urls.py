from django.urls import path

from .views import CarListView, CarPhotoUpdateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListView.as_view()),
    path('/<int:pk>/photo', CarPhotoUpdateView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view()),

]
