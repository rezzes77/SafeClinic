from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  DoctorCalendarViewSet

router = DefaultRouter()
router.register(r'calendar', DoctorCalendarViewSet, basename='doctor-calendar')


urlpatterns = [
    path('', include(router.urls)),
]
