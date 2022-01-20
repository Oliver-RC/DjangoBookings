from django.test import TestCase
from .forms import NewsletterSignUp


class TestNewsletterForm(TestCase):

    def test_item_first_name_is_required(self):
        form = NewsletterSignUp({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')

    def test_fields_are_all_included_in_form_metaclass(self):
        form = NewsletterSignUp()
        self.assertEqual(form.Meta.fields, '__all__')
