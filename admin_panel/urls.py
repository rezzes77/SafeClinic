from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, BranchViewSet, PatientViewSet, ServiceViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'branches', BranchViewSet, basename='branches')
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'categories', CategoryViewSet, basename='categories')


urlpatterns = [
    path('', include(router.urls)),

]