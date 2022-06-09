from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required,user_passes_test

from .forms import (DoctorMoreModelForm, LoginForm, PatientMoreModelForm, CustomRegistrationForm)


class PatientLoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/patient/login.html'
    success_url = reverse_lazy('accounts:patient_profile')
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True 
        else:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False 
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.type == 'PATIENT':
                login(self.request, user)
                return redirect('accounts:patient_profile')
            messages.add_message(self.request, messages.INFO, 'User doesn\'t exists!')
            return redirect('accounts:patient_login')
        return super().form_valid(form)


def check_patient_user(user):
    return user.type == 'PATIENT'

    
@login_required(login_url='accounts:patient_login')
@user_passes_test(check_patient_user, login_url='accounts:patient_login')
def patient_profile_view(request):
    if request.method == "POST":
        form = PatientMoreModelForm(request.POST, request.FILES, instance=request.user.patient_more)
        if form.is_valid():
            form.save()
    else:
        form = PatientMoreModelForm(instance=request.user.patient_more)
    return render(request, 'accounts/patient/profile.html', {'form': form})


class DoctorLoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/doctor/login.html'
    success_url = reverse_lazy('accounts:doctor_profile')
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember_me']

        if not remember_me:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True 
        else:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False 

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.type == 'DOCTOR':
                login(self.request, user)
                return redirect('accounts:doctor_profile')
            messages.add_message(self.request, messages.INFO, 'User doesn\'t exists!')
            return redirect('accounts:doctor_login')
        return super().form_valid(form)


def check_doctor_user(user):
    return user.type == 'DOCTOR'
        

@login_required(login_url='accounts:doctor_login')
@user_passes_test(check_doctor_user, login_url='accounts:doctor_login')
def doctor_profile_view(request):
    if request.method == "POST":
        form = DoctorMoreModelForm(request.POST, request.FILES, instance=request.user.doctor_more)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Profile updated successfully!')
            return redirect('accounts:doctor_profile')
    form = DoctorMoreModelForm(instance=request.user.doctor_more)
    return render(request, 'accounts/doctor/profile.html', {'form': form})


@login_required(login_url='/')
def logged_out(request):
    user_type = request.user.type
    logout(request)
    if user_type== "PATIENT":
        return redirect('accounts:patient_login')
    else:
        return redirect('accounts:doctor_login')


class PatientRegistrationView(CreateView):
    form_class = CustomRegistrationForm
    template_name = 'accounts/patient/register.html'
    success_url = reverse_lazy('accounts:patient_login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.type = 'PATIENT'
        return super().form_valid(form)


class DoctorRegistrationView(CreateView):
    form_class = CustomRegistrationForm
    template_name = 'accounts/doctor/register.html'
    success_url = reverse_lazy('accounts:doctor_login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.type = 'DOCTOR'
        return super().form_valid(form)


class LoginPageView(TemplateView):
    template_name = 'accounts/loginpage.html'