from rest_framework import permissions
from company.models import company

class CompanyOwnerEditCancel(permissions.BasePermission):
    edit_methods = ('PUT', 'PATCH')

    def has_permission(self, request, view):
       if request.user.is_authenticated:
           return True
       
    def has_object_permission(self, request, view, obj):        
        #current_company = company.objects.get(system_user_id=request.user.id)   
        if obj.system_user_id_id != request.user.id:
            return False
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True       
        if request.user.is_staff and request.method not in self.edit_methods:
            return True
        return False