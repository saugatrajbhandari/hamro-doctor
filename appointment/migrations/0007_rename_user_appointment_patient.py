# Generated by Django 4.0.4 on 2022-06-09 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_alter_appointment_doctor_alter_appointment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='user',
            new_name='patient',
        ),
    ]
