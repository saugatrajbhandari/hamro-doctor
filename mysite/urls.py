from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls', namespace='homepage')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('appointment/', include('appointment.urls', namespace='appointment')),
    path('hospital/', include('hospital.urls', namespace='hospital')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)