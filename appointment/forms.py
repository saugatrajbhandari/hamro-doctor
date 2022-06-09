from django import forms 

from .models import Appointment

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class PatientAppointmentModelForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appt_date', 'timing']
        widgets = {
            'appt_date': DateInput(),
            'timing': TimeInput()
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['appt_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['timing'].widget.attrs.update({'class': 'form-control'})


class DoctorAppointmentModelForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appt_date', 'timing', 'status']
        widgets = {
            'appt_date': DateInput(),
            'timing': TimeInput()
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['appt_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['timing'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})