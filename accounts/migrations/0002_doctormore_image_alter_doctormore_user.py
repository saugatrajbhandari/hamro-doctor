# Generated by Django 4.0.4 on 2022-05-28 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctormore',
            name='image',
            field=models.ImageField(blank=True, default='default_user.png', null=True, upload_to='doctor_profile', verbose_name='Profile image'),
        ),
        migrations.AlterField(
            model_name='doctormore',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_more', to=settings.AUTH_USER_MODEL),
        ),
    ]
