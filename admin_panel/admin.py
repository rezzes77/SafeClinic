from django.contrib import admin
from .models import Doctor, Branch, Patient, Service

admin.site.register(Doctor)
admin.site.register(Branch)
admin.site.register(Patient)
admin.site.register(Service)
