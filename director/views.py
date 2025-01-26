from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .filters import DoctorFilter
from rest_framework import viewsets
from .serializers import DoctorDirSerializer
from .models import DoctorDir


class DoctorDirViewSet(viewsets.ModelViewSet):
    queryset = DoctorDir.objects.all()
    serializer_class = DoctorDirSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DoctorFilter

