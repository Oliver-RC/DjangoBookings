from django.test import TestCase
from .models import Menu, Category


class TestViews(TestCase):

    def test_get_menu(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
