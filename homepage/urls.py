from django.urls import path 

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
]
