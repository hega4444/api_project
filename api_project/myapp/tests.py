# myapp/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Person

class PersonAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person_url = reverse('person-list-create')

    def test_create_person(self):
        data = {
            'first_name': 'John',
            'last_name': 'doe',
            'age': 30,
            'height': 180.0,
            'weight': 70.0,
            'hair_color': 'Brown',
            'eye_color': 'Blue',
            'distinctive_features': 'Scar on left cheek',
        }

        response = self.client.post(self.person_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().first_name, 'John')
        self.assertEqual(Person.objects.get().last_name, 'Doe')  

    def test_get_person_list(self):
        response = self.client.get(self.person_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Person.objects.count())

    # Add more test cases as needed
