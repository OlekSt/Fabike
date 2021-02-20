from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User
from django.test.client import Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('admin', 'admin@wizards.com', 'adminpass')

    def test_get_bikes_page(self):
        response = self.client.get("/products/bikes/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/bikes.html")

    def test_get_urban_page(self):
        response = self.client.get("/products/urban/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/urban.html")

    def test_get_all_road_page(self):
        response = self.client.get("/products/all_road/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/all_road.html")

    def test_get_road_page(self):
        response = self.client.get("/products/road/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/road.html")

    def test_get_product_page(self):
        product = Product.objects.create()
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product.html")

    def test_get_add_product_page(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/add_product.html")

    def test_get_edit_product_page(self):
        self.client.login(username='admin', password='adminpass')
        product = Product.objects.create()
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/edit_product.html")

    def test_get_delete_product_page(self):
        self.client.login(username='admin', password='adminpass')
        product = Product.objects.create()
        response = self.client.get(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/products/bikes/')
        existing_products = Product.objects.filter(id=product.id)
        self.assertEqual(len(existing_products), 0)
