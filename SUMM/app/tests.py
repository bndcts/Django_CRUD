from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserTests(APITestCase):
    def setUp(self):
        #c = Client()
        # response = c.post('/api/users/add', {"name": "Benedikt", "QuotaSpent": 10, "QuotaLimit": 11})
        self.data = {
            "Name": "Benedikt",
            "QuotaLimit": 11,
            "QuotaSpent": 0,
        }
        self.response = self.client.post(
            reverse('add-user'),
            self.data,
            format="json")


    def test_api_create_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().Name, 'Benedikt')

    def test_api_create_existing_user(self):
        url = reverse('add-user')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)