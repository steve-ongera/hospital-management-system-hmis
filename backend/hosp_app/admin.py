from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Patient, Appointment, MedicalRecord, Medication, Prescription


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']
    list_filter = ['role', 'is_staff', 'is_active']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Information', {'fields': ('role', 'phone')}),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Role Information', {'fields': ('role', 'phone')}),
    )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone', 'created_at']
    list_filter = ['gender', 'blood_group', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone', 'email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 'blood_group')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email', 'address')
        }),
        ('System Information', {
            'fields': ('created_by', 'created_at', 'updated_at')
        }),
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'appointment_date', 'appointment_time', 'status', 'created_at']
    list_filter = ['status', 'appointment_date', 'doctor']
    search_fields = ['patient__first_name', 'patient__last_name', 'doctor__username']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Appointment Details', {
            'fields': ('patient', 'doctor', 'appointment_date', 'appointment_time', 'reason')
        }),
        ('Status', {
            'fields': ('status', 'notes')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['patient', 'recorded_by', 'created_at']
    list_filter = ['created_at', 'recorded_by']
    search_fields = ['patient__first_name', 'patient__last_name', 'diagnosis']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Patient Information', {
            'fields': ('patient', 'recorded_by')
        }),
        ('Medical Information', {
            'fields': ('diagnosis', 'symptoms', 'treatment')
        }),
        ('Vital Signs', {
            'fields': ('temperature', 'blood_pressure', 'heart_rate')
        }),
        ('Additional Notes', {
            'fields': ('notes',)
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'unit_price', 'stock_quantity', 'created_at']
    list_filter = ['manufacturer', 'created_at']
    search_fields = ['name', 'manufacturer', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Medication Information', {
            'fields': ('name', 'description', 'manufacturer')
        }),
        ('Inventory', {
            'fields': ('unit_price', 'stock_quantity')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'medication', 'quantity', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'doctor']
    search_fields = ['patient__first_name', 'patient__last_name', 'medication__name']
    readonly_fields = ['created_at', 'updated_at', 'dispensed_at']
    
    fieldsets = (
        ('Prescription Details', {
            'fields': ('patient', 'doctor', 'medication')
        }),
        ('Dosage Information', {
            'fields': ('dosage', 'frequency', 'duration', 'quantity', 'instructions')
        }),
        ('Status', {
            'fields': ('status', 'dispensed_by', 'dispensed_at')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at')
        }),
    )