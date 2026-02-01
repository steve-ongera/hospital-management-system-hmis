from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime

from .models import Patient, Appointment, MedicalRecord, Medication, Prescription
from .serializers import (
    UserSerializer, UserRegistrationSerializer,
    PatientSerializer, AppointmentSerializer, AppointmentListSerializer,
    MedicalRecordSerializer, MedicationSerializer, PrescriptionSerializer,
    PrescriptionDispenseSerializer
)
from .permissions import (
    IsDoctor, IsNurse, IsPharmacist, IsDoctorOrNurse,
    IsDoctorOrReadOnly, IsPharmacistOrReadOnly
)

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistrationSerializer
        return UserSerializer
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Get current user profile"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsDoctorOrNurse]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        queryset = Patient.objects.all()
        
        # Filter by search query
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                first_name__icontains=search
            ) | queryset.filter(
                last_name__icontains=search
            )
        
        return queryset
    
    @action(detail=True, methods=['get'])
    def appointments(self, request, pk=None):
        """Get all appointments for a patient"""
        patient = self.get_object()
        appointments = patient.appointments.all()
        serializer = AppointmentListSerializer(appointments, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def medical_records(self, request, pk=None):
        """Get all medical records for a patient"""
        patient = self.get_object()
        records = patient.medical_records.all()
        serializer = MedicalRecordSerializer(records, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def prescriptions(self, request, pk=None):
        """Get all prescriptions for a patient"""
        patient = self.get_object()
        prescriptions = patient.prescriptions.all()
        serializer = PrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsDoctorOrNurse]
    
    def get_queryset(self):
        queryset = Appointment.objects.all()
        user = self.request.user
        
        # Doctors see only their appointments
        if user.role == 'doctor':
            queryset = queryset.filter(doctor=user)
        
        # Filter by status
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        # Filter by date
        date_filter = self.request.query_params.get('date', None)
        if date_filter:
            queryset = queryset.filter(appointment_date=date_filter)
        
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AppointmentListSerializer
        return AppointmentSerializer
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Mark appointment as completed"""
        appointment = self.get_object()
        appointment.status = 'completed'
        appointment.save()
        serializer = self.get_serializer(appointment)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """Cancel appointment"""
        appointment = self.get_object()
        appointment.status = 'cancelled'
        appointment.save()
        serializer = self.get_serializer(appointment)
        return Response(serializer.data)


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated, IsDoctorOrNurse]
    
    def perform_create(self, serializer):
        serializer.save(recorded_by=self.request.user)
    
    def get_queryset(self):
        queryset = MedicalRecord.objects.all()
        
        # Filter by patient
        patient_id = self.request.query_params.get('patient', None)
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        
        return queryset


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated, IsPharmacistOrReadOnly]
    
    def get_queryset(self):
        queryset = Medication.objects.all()
        
        # Filter by search query
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        
        # Filter by low stock
        low_stock = self.request.query_params.get('low_stock', None)
        if low_stock == 'true':
            queryset = queryset.filter(stock_quantity__lt=10)
        
        return queryset
    
    @action(detail=True, methods=['post'])
    def update_stock(self, request, pk=None):
        """Update medication stock"""
        medication = self.get_object()
        quantity = request.data.get('quantity', 0)
        
        try:
            quantity = int(quantity)
            medication.stock_quantity += quantity
            medication.save()
            serializer = self.get_serializer(medication)
            return Response(serializer.data)
        except (ValueError, TypeError):
            return Response(
                {'error': 'Invalid quantity'},
                status=status.HTTP_400_BAD_REQUEST
            )


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [IsAuthenticated(), IsDoctor()]
        elif self.action == 'dispense':
            return [IsAuthenticated(), IsPharmacist()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        queryset = Prescription.objects.all()
        user = self.request.user
        
        # Doctors see only their prescriptions
        if user.role == 'doctor':
            queryset = queryset.filter(doctor=user)
        
        # Pharmacists see pending prescriptions
        if user.role == 'pharmacist':
            status_filter = self.request.query_params.get('status', 'pending')
            if status_filter:
                queryset = queryset.filter(status=status_filter)
        
        # Filter by patient
        patient_id = self.request.query_params.get('patient', None)
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        
        return queryset
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsPharmacist])
    def dispense(self, request, pk=None):
        """Dispense prescription (pharmacist only)"""
        prescription = self.get_object()
        
        if prescription.status == 'dispensed':
            return Response(
                {'error': 'Prescription already dispensed'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if prescription.status == 'cancelled':
            return Response(
                {'error': 'Cannot dispense cancelled prescription'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check stock
        medication = prescription.medication
        if medication.stock_quantity < prescription.quantity:
            return Response(
                {'error': f'Insufficient stock. Available: {medication.stock_quantity}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Update prescription
        prescription.status = 'dispensed'
        prescription.dispensed_by = request.user
        prescription.dispensed_at = timezone.now()
        prescription.save()
        
        # Update medication stock
        medication.stock_quantity -= prescription.quantity
        medication.save()
        
        serializer = self.get_serializer(prescription)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsDoctor])
    def cancel(self, request, pk=None):
        """Cancel prescription (doctor only)"""
        prescription = self.get_object()
        
        if prescription.status == 'dispensed':
            return Response(
                {'error': 'Cannot cancel dispensed prescription'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        prescription.status = 'cancelled'
        prescription.save()
        
        serializer = self.get_serializer(prescription)
        return Response(serializer.data)