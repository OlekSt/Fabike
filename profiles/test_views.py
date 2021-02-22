from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('user',
                                             'user@elves.com',
                                             'userpass')

    def test_get_profile_page(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
