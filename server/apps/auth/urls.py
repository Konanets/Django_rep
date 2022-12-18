from django.urls import path

from .views import ActivateUserView, ChangePasswordView, RecoveryPasswordView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/recovery', RecoveryPasswordView.as_view()),
    path('/change/<str:token>', ChangePasswordView.as_view())
]
