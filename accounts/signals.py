# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings

# from .models import PatientMore

# User = settings.AUTH_USER_MODEL


# @receiver(post_save, sender=User)
# def create_patient_profile(sender, instance, created, **kwargs):
#     if created :
#         PatientMore.objects.create(user=instance)

#     instance.patient_more.save()