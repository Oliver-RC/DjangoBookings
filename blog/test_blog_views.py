from django.test import TestCase
from .models import Post


class TestViews(TestCase):

    def test_get_blog(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')
