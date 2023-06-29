from rest_framework import permissions


class StudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user.is_superuser
        except AttributeError:
            if request.method == "POST":
                return True
            return False
