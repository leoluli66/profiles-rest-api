from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: #HTTP GET method is safe
            return True

        return obj.id == request.user.id #if the request id matches the object'id, since user can only update its own profiles


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is tring to update their own staus"""
        if request.method in permissions.SAFE_METHODS: #HTTP GET method is safe
            return True

        return obj.user_profile.id == request.user.id #Put, patch, delete
