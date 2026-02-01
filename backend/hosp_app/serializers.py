from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Patient, Appointment, MedicalRecord, Medication, Prescription

User = get_user_model()


# User Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'phone']
        read_only_fields = ['id']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role', 'phone']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data['role'],
            phone=validated_data.get('phone', '')
        )
        return user


# Patient Serializers
class PatientSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    age = serializers.SerializerMethodField()
    
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by']
    
    def get_age(self, obj):
        from datetime import date
        today = date.today()
        age = today.year - obj.date_of_birth.year - ((today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day))
        return age


# Appointment Serializers
class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.first_name', read_only=True)
    patient_full = serializers.SerializerMethodField()
    doctor_name = serializers.CharField(source='doctor.get_full_name', read_only=True)
    
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_patient_full(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"
    
    def validate(self, data):
        # Ensure doctor has doctor role
        if data.get('doctor') and data['doctor'].role != 'doctor':
            raise serializers.ValidationError("Only users with doctor role can be assigned to appointments.")
        return data


class AppointmentListSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    doctor_name = serializers.CharField(source='doctor.get_full_name', read_only=True)
    
    class Meta:
        model = Appointment
        fields = ['id', 'patient_name', 'doctor_name', 'appointment_date', 'appointment_time', 'status', 'reason']
    
    def get_patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"


# Medical Record Serializers
class MedicalRecordSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    recorded_by_name = serializers.CharField(source='recorded_by.get_full_name', read_only=True)
    
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'recorded_by']
    
    def get_patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"


# Medication Serializers
class MedicationSerializer(serializers.ModelSerializer):
    stock_status = serializers.SerializerMethodField()
    
    class Meta:
        model = Medication
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_stock_status(self, obj):
        if obj.stock_quantity == 0:
            return 'out_of_stock'
        elif obj.stock_quantity < 10:
            return 'low_stock'
        return 'in_stock'


# Prescription Serializers
class PrescriptionSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    doctor_name = serializers.CharField(source='doctor.get_full_name', read_only=True)
    medication_name = serializers.CharField(source='medication.name', read_only=True)
    dispensed_by_name = serializers.CharField(source='dispensed_by.get_full_name', read_only=True)
    
    class Meta:
        model = Prescription
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'dispensed_by', 'dispensed_at']
    
    def get_patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"
    
    def validate(self, data):
        # Ensure doctor has doctor role
        if data.get('doctor') and data['doctor'].role != 'doctor':
            raise serializers.ValidationError("Only users with doctor role can create prescriptions.")
        
        # Check medication stock when creating
        if self.instance is None:  # Creating new prescription
            medication = data.get('medication')
            quantity = data.get('quantity', 0)
            if medication and medication.stock_quantity < quantity:
                raise serializers.ValidationError(f"Insufficient stock. Available: {medication.stock_quantity}")
        
        return data


class PrescriptionDispenseSerializer(serializers.Serializer):
    """Serializer for dispensing prescriptions"""
    prescription_id = serializers.IntegerField()
    
    def validate_prescription_id(self, value):
        try:
            prescription = Prescription.objects.get(id=value)
            if prescription.status == 'dispensed':
                raise serializers.ValidationError("Prescription already dispensed.")
            if prescription.status == 'cancelled':
                raise serializers.ValidationError("Cannot dispense cancelled prescription.")
        except Prescription.DoesNotExist:
            raise serializers.ValidationError("Prescription not found.")
        return value