from urllib import response
from django.test import TestCase

from django.contrib.auth import get_user_model

User = get_user_model()


class AppointmentTestCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'saugat',
            'password': 'saugat'
        }

        User.objects.create_user(**self.credentials, type="PATIENT")
    
    def test_login(self):
        response = self.client.post('/accounts/patient/login/', username="saugat", password="saugat")
        print(response)
        print(response.context['user'])
        self.assertTrue(response.context['user'].is_active)
    

        