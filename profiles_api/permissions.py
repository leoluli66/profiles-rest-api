from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: #HTTP GET method is safe
            return True

        return obj.id == request.user.id #if the request id matches the object'id, since user can only update its own profiles
