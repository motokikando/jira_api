from rest_framework import permissions

class IntroducerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.introducer.id == request.user.id
