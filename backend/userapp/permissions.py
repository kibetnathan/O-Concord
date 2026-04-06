from rest_framework.permissions import BasePermission

class IsAuthorOrPastor(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.groups.filter(name="Pastor").exists():
            return True

        return obj.author == request.user
