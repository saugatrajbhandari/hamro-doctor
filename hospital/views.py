from django.shortcuts import render

from django.views.generic import DetailView, ListView

from hospital.models import Hospital


class HospitalDetailView(DetailView):
    queryset = Hospital.objects.all()
    context_object_name = "hospital"
    template_name = 'hospital/hospital_detail.html'


class HospitalListView(ListView):
    queryset = Hospital.objects.all()
    context_object_name = "hospitals"
    template_name = "hospital/hospital_list.html"
    paginate_by = 6