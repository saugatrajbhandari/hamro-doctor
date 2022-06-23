from django.db import models

from ckeditor.fields import RichTextField


class Hospital(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    services = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='hospital', default="hospital/hospital.jpg")
    contact_number = models.CharField('Contact Number', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
