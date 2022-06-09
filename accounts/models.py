from operator import mod
from turtle import pos
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_patient_profile(sender, instance, created, **kwargs):
    if instance.type == 'PATIENT':
        if created:
            PatientMore.objects.create(user=instance)

        instance.patient_more.save()


@receiver(post_save, sender=User)
def create_doctor_profile(sender, instance, created, **kwargs):
    if instance.type == 'DOCTOR':
        if created:
            DoctorMore.objects.create(user=instance)
        
        instance.doctor_more.save()


class User(AbstractUser):

    class Types(models.TextChoices):
        PATIENT = 'PATIENT', 'patient'
        DOCTOR = 'DOCTOR', 'doctor'
        MERCHANT = 'MERCHANT', 'merchant'
    phone = models.CharField('Phone Number', unique=True, max_length=15, null=True, blank=True)
    full_name = models.CharField('Full Name', max_length=255, null=True, blank=True)
    type = models.CharField(max_length=10, choices=Types.choices, default=Types.PATIENT)

    REQUIRED_FIELDS = []


class PatientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PATIENT)


class Patient(User):
    objects = PatientManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PATIENT
        return super().save(*args, **kwargs)


class PatientMore(models.Model):

    class Gender(models.TextChoices):
        MALE = 'MALE', 'Male'
        FEMALE = 'FEMALE', 'Female'
        OTHERS = 'OTHERS', 'Others'

    class BloodGroup(models.TextChoices):
        A_POSITIVE = 'A+', 'A+'
        A_NEGATIVE = 'A-', 'A-'
        B_POSITIVE = 'B+', 'B+'
        B_NEGATIVE = 'B-', 'B-'
        AB_POSITIVE = 'AB+', 'AB+'
        AB_NEGATIVE = 'AB-', 'AB-'
        O_POSITIVE = 'O+', 'O+'
        O_NEGATIVE = 'O-', 'O-'



    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_more')

    image = models.ImageField('Profile image', upload_to='patient_profile', default='default_user.png', null=True, blank=True)
    address = models.CharField('Address', max_length=255, blank=True, null=True)
    dob = models.DateField('Date of birth', null=True, blank=True)
    gender = models.CharField('Gender', max_length=10, choices=Gender.choices, default=Gender.MALE)
    blood_group = models.CharField('Blood Group', max_length=15, choices=BloodGroup.choices, default=BloodGroup.A_POSITIVE)
    weight = models.FloatField('Weight', null=True, blank=True)
    height = models.FloatField('Height', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

        

class DoctorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DOCTOR)


class DoctorMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_more')
    image = models.ImageField('Profile image', upload_to='doctor_profile', default='default_user.png', null=True, blank=True)
    short_bio = models.CharField('Short bio', max_length=255, null=True, blank=True)
    nmc_number = models.IntegerField('NMC Number', null=True, blank=True)
    description = models.TextField('Description', null=True, blank=True)
    # available_locations
    specialization = models.TextField('Specialization', null=True, blank=True)
    # exprience
    # education
    # awards
    # research journals
    # membership


class Doctor(User):
    objects = DoctorManager()
    class Meta:
        proxy = True

    @property
    def more(self):
        return self.doctormore

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.DOCTOR
        return super().save(*args, **kwargs)



class MerchantManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.MERCHANT)


class Merchant(User):
    objects = MerchantManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.MERCHANT
        return super().save(*args, **kwargs)