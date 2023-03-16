from unittest import TestCase

from rest_api.models import Teacher
from rest_framework.test import APIRequestFactory, APITestCase

from rest_api.views import TeacherList


class TeacherListViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_teachers = 30
        for student_id in range(number_of_teachers):
            Teacher.objects.create(name=f"proful_{student_id}", email=f"prof.{student_id}@ubbcluj.ro", address="Cluj-Napoca")

    def test_url_exists(self):
        response = self.client.get("/api/teachers/")

        self.assertEqual(response.status_code, 200)

    def test_count_correctly_returned(self):
        response = self.client.get("/api/teachers/")
        self.assertEqual(len(response.data), 30)

