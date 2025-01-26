from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentListSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name')
    doctor_name = serializers.CharField(source='doctor.full_name')

    class Meta:
        model = Appointment
        fields = ['date', 'service_name', 'doctor_name', 'complains']

