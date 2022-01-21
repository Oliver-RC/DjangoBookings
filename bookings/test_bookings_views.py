from django.test import TestCase
from .models import Booking


class TestViews(TestCase):

    def test_get_booking(self):
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')
