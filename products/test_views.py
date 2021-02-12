from django.test import TestCase

class TestProductsViews(TestCase):

    def test_get_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/bikes.html")
        self.assertTemplateUsed(response, "products/urban.html")
        self.assertTemplateUsed(response, "products/road.html")
        self.assertTemplateUsed(response, "products/all_road.html")
        self.assertTemplateUsed(response, "products/frames.html")
        self.assertTemplateUsed(response, "products/product.html")