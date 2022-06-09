from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import ListView

def home(request):
    doctors = get_user_model().objects.filter(type='DOCTOR')[:4 ]
    return render(request, 'homepage/home.html', {'doctors': doctors})


class DoctorListView(ListView):
    model = get_user_model()
    template_name = 'homepage/doctors.html'
    context_object_name = 'doctors'
    paginate_by = 6 

    def get_queryset(self):
        return self.model.objects.filter(type='DOCTOR')