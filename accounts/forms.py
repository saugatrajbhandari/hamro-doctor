from django import forms 
from django.contrib.admin.widgets import AdminDateWidget

from .models import PatientMore, DoctorMore


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    remember_me = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['remember_me'].widget.attrs.update({'label': 'Remember me'})



class DobInput(forms.DateInput):
    input_type = 'date'

class PatientMoreModelForm(forms.ModelForm):
    dob = forms.DateField(widget=DobInput)
    class Meta:
        model = PatientMore
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['dob'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['blood_group'].widget.attrs.update({'class': 'form-control'})
        self.fields['weight'].widget.attrs.update({'class': 'form-control'})
        self.fields['height'].widget.attrs.update({'class': 'form-control'})
        



class DoctorMoreModelForm(forms.ModelForm):
    class Meta:
        model = DoctorMore
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['short_bio'].widget.attrs.update({'class': 'form-control'})
        self.fields['nmc_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['specialization'].widget.attrs.update({'class': 'form-control'})
