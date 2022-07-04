from rest_framework import permissions


class UsageManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class UpdateManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        elif request.method == 'PUT' or 'PATCH':
            return bool(request.user and request.user.is_staff)


class FeedbackM(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return True

        elif request.method == 'GET':
            return bool(request.user and request.user.is_staff)
