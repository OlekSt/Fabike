from django.test import TestCase
from .models import Product


class TestModels(TestCase):
    def test_is_bike_defaults_to_true(self):
        product = Product.objects.create()
        self.assertTrue(product.is_bike)
