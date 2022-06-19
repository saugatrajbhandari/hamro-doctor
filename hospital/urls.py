from django.urls import path

from . import views

app_name = 'hospital'

urlpatterns = [
    path('<int:pk>/', views.HospitalDetailView.as_view(), name="hospital_detail"),
    path('', views.HospitalListView.as_view(), name="hospital_list"),

]
