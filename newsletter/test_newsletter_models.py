from django.test import TestCase
from .models import Newsletter


class TestModels(TestCase):

    def test_first_name_defaults_to_true(self):
        name = Newsletter.objects.create(first_name='Person A')
        self.assertTrue(name.first_name)

    def test_newsletter_string_method_returns_first_name(self):
        name = Newsletter.objects.create(first_name='Person A')
        self.assertEqual(str(name), 'Person A')