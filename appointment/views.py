from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

from .forms import PatientAppointmentModelForm, DoctorAppointmentModelForm
from .models import Appointment


User = get_user_model()

class PatientMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.type == 'PATIENT'

    def handle_no_permission(self):
        return redirect('appointment:permission_forbidden')


class DoctorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.type == 'DOCTOR'

    def handle_no_permission(self):
        return redirect('appointment:permission_forbidden')


class PermissionForbidden(generic.TemplateView):
    template_name = 'appointment/utils/custom_forbidden.html'


class PatientAppointmentView(LoginRequiredMixin, PatientMixin, generic.CreateView):
    model = Appointment
    form_class = PatientAppointmentModelForm
    template_name = 'appointment/appointment.html'
    success_url = reverse_lazy('homepage:home')

    def form_valid(self, form):
        doctor = User.objects.get(id=self.kwargs.get('pk'))
        form.instance.user = self.request.user
        form.instance.doctor = doctor
        return super().form_valid(form)


class PatientAppointment(LoginRequiredMixin,PatientMixin,generic.ListView):
    template_name = 'appointment/patient_appointment.html'
    context_object_name = 'appointments'

    def get_queryset(self, *args, **kwargs):
        return self.request.user.appointment_patient.all()


class DoctorAppointment(LoginRequiredMixin,DoctorMixin,generic.ListView):
    template_name = 'appointment/doctor_appointment.html'
    context_object_name = 'appointments'

    def get_queryset(self, *args, **kwargs):
        return self.request.user.appointment_doctor.all()


class DoctorAppointmentUpdateView(LoginRequiredMixin,DoctorMixin,generic.UpdateView):

    form_class = DoctorAppointmentModelForm
    template_name = 'appointment/doctor_appointment_update.html'
    success_url = reverse_lazy('appointment:doctor_appointment')

    def get_queryset(self, *args, **kwargs):
        return self.request.user.appointment_doctor.all()


class PatientAppointmentUpdateView(LoginRequiredMixin,PatientMixin,generic.UpdateView):

    form_class = PatientAppointmentModelForm
    template_name = 'appointment/patient_appointment_update.html'
    success_url = reverse_lazy('appointment:patient_appointment')

    def get_queryset(self, *args, **kwargs):
        return self.request.user.appointment_patient.all()


class PatientAppointmentDeleteView(LoginRequiredMixin, PatientMixin, generic.DeleteView):
    template_name = 'appointment/patient_appointment_delete_confrim.html'
    success_url = reverse_lazy('appointment:patient_appointment')

    def get_queryset(self, *args, **kwargs):
        return self.request.user.appointment_patient.all()
