from pydoc import Doc
from django.db import models
from django.conf import settings
from accounts.models import Doctor, Patient


class Appointment(models.Model):

    class STATUS(models.TextChoices):
        PENDING = 'PENDING', 'pending'
        CONFIRM = 'CONFIRM', 'confrim'

    appt_date = models.DateField('Appointment date', null=True, blank=True)
    timing = models.TimeField('Timing', null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS.choices, default=STATUS.PENDING)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, related_name='appointment_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='appointment_doctor')


    def __str__(self):
        return f"{self.patient.username}-{self.id} appointment"