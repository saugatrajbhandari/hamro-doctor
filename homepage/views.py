from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.db.models import Q

from hospital.models import Hospital

def home(request):
    doctors = get_user_model().objects.filter(type='DOCTOR')[:4 ]
    hospitals = Hospital.objects.all()[:6]
    print(hospitals)
    data = request.GET.get('q')
    if data:
        doctors_search = get_user_model().objects.filter(type='DOCTOR')
        doctors = doctors_search.filter(Q(username__icontains=data) | Q(first_name__icontains=data) | Q(last_name__icontains=data))
        return render(request, 'homepage/search.html', {'doctors': doctors})
        
    return render(request, 'homepage/home.html', {'doctors': doctors, 'hospitals': hospitals})


class DoctorListView(ListView):
    model = get_user_model()
    template_name = 'homepage/doctors.html'
    context_object_name = 'doctors'
    paginate_by = 6 

    def get_queryset(self):
        return self.model.objects.filter(type='DOCTOR')