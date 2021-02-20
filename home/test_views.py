from django.test import TestCase


class TestViews(TestCase):
    def test_get_fabike(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_under_construction(self):
        response = self.client.get('/under_construction/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/under_construction.html')
