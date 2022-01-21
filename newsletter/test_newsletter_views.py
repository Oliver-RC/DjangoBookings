from django.test import TestCase
from .models import Newsletter


class TestViews(TestCase):

    def test_get_newsletter(self):
        response = self.client.get('/newsletter/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter.html')
