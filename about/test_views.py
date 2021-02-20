from django.test import TestCase


class TestViews(TestCase):
    def test_get_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
