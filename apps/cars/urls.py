from django.urls import path

from .views import CarListCreateView, CarListRetrieveUpdateDestroy

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarListRetrieveUpdateDestroy.as_view())
]
