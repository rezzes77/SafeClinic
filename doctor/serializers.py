from rest_framework import serializers
from client.models import Appointment

class DoctorCalendarSerializer(serializers.ModelSerializer):
    previous = serializers.SerializerMethodField()
    next = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['id', 'full_name', 'service', 'doctor', 'date', 'time', 'complains', 'phone_number', 'address', 'previous', 'next']

    def get_previous(self, obj):
        previous_appointment = Appointment.objects.filter(doctor=obj.doctor, date__lt=obj.date).order_by('-date', '-time').first()
        return {
            "date": previous_appointment.date,
            "time": previous_appointment.time
        } if previous_appointment else None

    def get_next(self, obj):
        next_appointment = Appointment.objects.filter(doctor=obj.doctor, date__gt=obj.date).order_by('date', 'time').first()
        return {
            "date": next_appointment.date,
            "time": next_appointment.time
        } if next_appointment else None

    def validate(self, data):
        if Appointment.objects.filter(date=data['date'], time=data['time'], doctor=data['doctor']).exists():
            raise serializers.ValidationError("Этот временной слот уже занят. Выберите другое время.")
        return data