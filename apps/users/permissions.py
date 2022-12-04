from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsSuperUser(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaff(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(request.user and request.user.is_staff)
