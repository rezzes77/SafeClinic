"""
URL configuration for SafeClinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from admin_panel.views import DoctorViewSet, BranchViewSet, PatientViewSet, ServiceViewSet, CategoryViewSet, DirectorViewSet
from client.views import AppointmentViewSet, AppointmentListViewSet
from doctor.views import  DoctorCalendarViewSet
from smtp.views import RegisterViewSet, LoginViewSet


router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'directors', DirectorViewSet, basename='directors')
router.register(r'branches', BranchViewSet, basename='branches')
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'appointments', AppointmentViewSet, basename='appointments')
router.register(r'appointments-list', AppointmentListViewSet, basename='appointments-list')
router.register(r'calendar', DoctorCalendarViewSet, basename='doctor-calendar')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'profiles', RegisterViewSet, basename='profiles')


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/admin/', include('admin_panel.urls')),
    # path('api/doctor/', include('doctor.urls')),
    # path('api/director/', include('director.urls')),
    # path('api/client/', include('client.urls')),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^client/', include('client.urls')),
    path('api/', include(router.urls)),
    # path('smtp/', include('smtp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

