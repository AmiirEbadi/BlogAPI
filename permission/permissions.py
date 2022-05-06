from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)



class IsOwnerOrAdminOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            obj == request.user or request.user.is_superuser or
            request.method in SAFE_METHODS
        )


class IsWriterOrAdminOrReadonly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(
            request.user.Position == 'writer' or request.user.is_superuser
        )
        if request.method in SAFE_METHODS:
            return True
        return False
    

class IsAuthorOrAdminOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            obj.author == request.user or request.user.is_superuser or
            request.method in SAFE_METHODS
        )