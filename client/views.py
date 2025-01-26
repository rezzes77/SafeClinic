from django.shortcuts import render
from rest_framework import viewsets

from .serializers import AppointmentSerializer, AppointmentListSerializer
from .models import Appointment

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Appointment.objects.all().order_by('date')
    serializer_class = AppointmentListSerializer

