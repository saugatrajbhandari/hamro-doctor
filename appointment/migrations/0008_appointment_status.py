# Generated by Django 4.0.4 on 2022-06-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_rename_user_appointment_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('CONFIRM', 'confrim')], default='PENDING', max_length=15),
        ),
    ]