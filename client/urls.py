from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, AppointmentListViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointments')
router.register(r'appointments-list', AppointmentListViewSet, basename='appointments-list')

urlpatterns = [
    path('', include(router.urls)),

]