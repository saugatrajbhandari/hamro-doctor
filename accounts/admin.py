from django.contrib import admin

from .models import (User, Patient, PatientMore)

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(PatientMore)
