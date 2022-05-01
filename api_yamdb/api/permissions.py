from rest_framework import permissions


class RolePermission(permissions.BasePermission):
    """
    Разрешение на небезоспасные методы для определенных пользовательских ролей.
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.role in ('admin', 'moderator')
            or obj.author == request.user
        )
