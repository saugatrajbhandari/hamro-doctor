from django.urls import path

from . import views

app_name='accounts'

urlpatterns = [
    path('patient/login/', views.PatientLoginView.as_view(), name='patient_login'),
    path('patient/profile/', views.patient_profile_view, name='patient_profile'),
    path('patient/register/', views.PatientRegistrationView.as_view(), name='patient_register'),

    path('doctor/login/', views.DoctorLoginView.as_view(), name='doctor_login'),
    path('doctor/profile/', views.doctor_profile_view, name='doctor_profile'),
    path('doctor/register/', views.DoctorRegistrationView.as_view(), name='doctor_register'),

    path('logout/', views.logged_out, name='logout'),
]
