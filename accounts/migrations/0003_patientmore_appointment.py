# Generated by Django 4.0.4 on 2022-06-09 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
        ('accounts', '0002_doctormore_image_alter_doctormore_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientmore',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_more', to='appointment.appointment'),
        ),
    ]
