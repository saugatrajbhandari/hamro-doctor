from django.contrib import admin

from .models import (User, Patient, PatientMore, DoctorMore)

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(PatientMore)
admin.site.register(DoctorMore)
