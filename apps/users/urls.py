from django.urls import path

from .views import AddAutoParkView, AdminToUser, UserActivateView, UserCreateView, UserDeactivateView, UserToAdmin

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/auto_parks', AddAutoParkView.as_view()),
    path('/<int:pk>/activate', UserActivateView.as_view()),
    path('/<int:pk>/deactivate', UserDeactivateView.as_view()),
    path('/<int:pk>/to_admin', UserToAdmin.as_view()),
    path('/<int:pk>/to_user', AdminToUser.as_view())
]
