from django.test import TestCase


class TestViews(TestCase):
    def test_get_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
