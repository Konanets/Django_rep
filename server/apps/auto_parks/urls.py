from django.urls import path

from .views import AddCarToAutoParkView, AutoParkListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', AddCarToAutoParkView.as_view()),
]
