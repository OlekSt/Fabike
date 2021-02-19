from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    def test_item_frame_is_required(self):
        form = ProductForm({'frame': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('frame', form.errors.keys())
        self.assertEqual(form.errors['frame'][0], 'This field is required.')

    def test_item_name_is_required(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_item_title_is_required(self):
        form = ProductForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_item_fork_is_required(self):
        form = ProductForm({'fork': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('fork', form.errors.keys())
        self.assertEqual(form.errors['fork'][0], 'This field is required.')

    def test_item_brakes_is_required(self):
        form = ProductForm({'brakes': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('brakes', form.errors.keys())
        self.assertEqual(form.errors['brakes'][0], 'This field is required.')

    def test_item_image01_is_required(self):
        form = ProductForm({'image01': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('image01', form.errors.keys())
        self.assertEqual(form.errors['image01'][0], 'This field is required.')

    def test_item_image02_is_required(self):
        form = ProductForm({'image02': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('image02', form.errors.keys())
        self.assertEqual(form.errors['image02'][0], 'This field is required.')

    def fields_are_explicit_in_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, ['__all__'])
