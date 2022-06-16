from pydoc import doc
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import ListView

from django.db.models import Q

def home(request):
    doctors = get_user_model().objects.filter(type='DOCTOR')[:4 ]
    data = request.GET.get('q')
    if data:
        doctors_search = get_user_model().objects.filter(type='DOCTOR')
        doctors = doctors_search.filter(Q(username__icontains=data) | Q(first_name__icontains=data) | Q(last_name__icontains=data))
        # doctors = doctors_search.filter(Q(username__icontains=data))
        print(doctors)
        return render(request, 'homepage/search.html', {'doctors': doctors})
        
    return render(request, 'homepage/home.html', {'doctors': doctors})


class DoctorListView(ListView):
    model = get_user_model()
    template_name = 'homepage/doctors.html'
    context_object_name = 'doctors'
    paginate_by = 6 

    def get_queryset(self):
        return self.model.objects.filter(type='DOCTOR')