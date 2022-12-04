from django.urls import path

from .views import AddAutoParkView, MakeActiveView, MakeAdminView, UserCreateView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/auto_parks', AddAutoParkView.as_view()),
    path('/<int:pk>/active', MakeActiveView.as_view()),
    path('/<int:pk>/admin', MakeAdminView.as_view()),
]
