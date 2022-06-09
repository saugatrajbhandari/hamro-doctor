from django.urls import path

from . import views 

app_name = 'appointment'

urlpatterns = [
    path('book-appointment/<int:pk>/', views.PatientAppointmentView.as_view(), name='book_appointment'),

    path('permission-forbidden/', views.PermissionForbidden.as_view(), name='permission_forbidden'),

    path('patient-appointment/', views.PatientAppointment.as_view(), name='patient_appointment'),
    path('doctor-appointment/', views.DoctorAppointment.as_view(), name='doctor_appointment'),

    path('patient-appointment-update/<int:pk>/', views.PatientAppointmentUpdateView.as_view(), name='patient_appointment_update'),
    path('doctor-appointment-update/<int:pk>/', views.DoctorAppointmentUpdateView.as_view(), name='doctor_appointment_update'),

    path('patient-appointment-delete/<int:pk>/', views.PatientAppointmentDeleteView.as_view(), name='patient_appointment_delete'),
]
