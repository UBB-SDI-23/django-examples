from django.test import TestCase

from rest_api.models import Teacher


class TeacherModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Teacher.objects.create(name="Vlad", email="vlad.ionescu@ubbcluj.ro", address="Cluj-Napoca")

    def test_string_method(self):
        teacher = Teacher.objects.get(name="Vlad")
        expected_string = "Vlad"
        self.assertEqual(str(teacher), expected_string)

