from django.test import TestCase
from .forms import EventForm


class TestEventForm(TestCase):
    def test_item_title_is_required(self):
        form = EventForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_item_topics_is_required(self):
        form = EventForm({'topics': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('topics', form.errors.keys())
        self.assertEqual(form.errors['topics'][0], 'This field is required.')

    def test_item_learning_is_required(self):
        form = EventForm({'learning': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('learning', form.errors.keys())
        self.assertEqual(form.errors['learning'][0], 'This field is required.')

    def test_item_date_is_required(self):
        form = EventForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_item_time_is_required(self):
        form = EventForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')

    def test_item_address_is_required(self):
        form = EventForm({'address': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('address', form.errors.keys())
        self.assertEqual(form.errors['address'][0], 'This field is required.')

    def test_item_town_or_city_is_required(self):
        form = EventForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0], 'This field is required.')
    
    def test_item_price_is_required(self):
        form = EventForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def fields_are_explicit_in_metaclass(self):
        form = EventForm()
        self.assertEqual(form.Meta.fields, ['title', 'topics', 'learning', 'date', 'time', 'address', 'town_or_city', 'price'])
