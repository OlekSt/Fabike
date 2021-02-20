from django.test import TestCase
from .forms import ProfileForm


class TestProfileForm(TestCase):
    def fields_are_explicit_in_metaclass(self):
        form = ProfileForm()
        self.assertEqual(form.Meta.fields, ['user_phone_number', 'user_postcode', 'user_address_line1','user_address_line2', 'user_county'])
