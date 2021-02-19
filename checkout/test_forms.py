from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    def test_item_full_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')

    def test_item_email_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_item_phone_number_is_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0], 'This field is required.')

    def test_item_address_line1_is_required(self):
        form = OrderForm({'address_line1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('address_line1', form.errors.keys())
        self.assertEqual(form.errors['address_line1'][0], 'This field is required.')

    def test_item_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0], 'This field is required.')

    def fields_are_explicit_in_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ['full_name', 'email', 'phone_number', 'address_line1', 'address_line2',
        'town_or_city', 'postcode', 'county', 'country'])
