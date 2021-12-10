from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'user is not the author'

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request

        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user


class ApiPermissions(permissions.BasePermission):
    message = 'Custom Permissions '

    def admin_user(self, request):
        user = self.request.user
        user.is_superuser()
        return True


class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False
