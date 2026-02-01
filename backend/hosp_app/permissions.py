from rest_framework import permissions


class IsDoctor(permissions.BasePermission):
    """
    Permission check for Doctor role
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'doctor'


class IsNurse(permissions.BasePermission):
    """
    Permission check for Nurse role
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'nurse'


class IsPharmacist(permissions.BasePermission):
    """
    Permission check for Pharmacist role
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'pharmacist'


class IsDoctorOrNurse(permissions.BasePermission):
    """
    Permission check for Doctor or Nurse role
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role in ['doctor', 'nurse']


class IsDoctorOrReadOnly(permissions.BasePermission):
    """
    Doctors can create/update, others can only read
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Read permissions for all authenticated users
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only for doctors
        return request.user.role == 'doctor'


class IsPharmacistOrReadOnly(permissions.BasePermission):
    """
    Pharmacists can create/update, others can only read
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Read permissions for all authenticated users
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only for pharmacists
        return request.user.role == 'pharmacist'