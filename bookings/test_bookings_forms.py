from django.test import TestCase
from .forms import BookingForm


class TestBookingForm(TestCase):

    def test_item_first_name_is_required(self):
        form = BookingForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')
    
    def test_exclude_are_excluded_in_form_metaclass(self):
            form = BookingForm()
            self.assertEqual(form.Meta.exclude, ['status', 'user'])