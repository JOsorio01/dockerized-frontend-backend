from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from employees.models import Area
from employees.serializers import AreaSerializer


class AreaTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_area(self):
        url = reverse('employees:area-list')
        payload = {'name': 'Area 1'}
        res = self.client.post(url, payload)

        area = Area.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(area.name, payload['name'])

    def test_partial_update_area(self):
        payload = {'name': 'New Area'}

        area = Area.objects.create(name="Area 1")
        url = reverse('employees:area-detail', args=[area.id])

        res = self.client.patch(url, payload)
        area.refresh_from_db()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(area.name, payload['name'])

    def test_full_update_area(self):
        payload = {'name': 'New Area'}

        area = Area.objects.create(name="Area 1")
        url = reverse('employees:area-detail', args=[area.id])

        res = self.client.put(url, payload)
        area.refresh_from_db()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(area.name, payload['name'])

    def test_detail_area(self):
        area = Area.objects.create(name="Area 1")
        url = reverse('employees:area-detail', args=[area.id])
        res = self.client.get(url)

        serializer = AreaSerializer(area)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data)

    def test_list_area(self):
        url = reverse('employees:area-list')
        Area.objects.create(name="Area 1")
        Area.objects.create(name="Area 2")

        res = self.client.get(url)

        areas = Area.objects.all()

        serializer = AreaSerializer(areas, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data)
