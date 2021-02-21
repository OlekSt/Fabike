from django.test import TestCase
from .models import Event
from django.contrib.auth.models import User
from django.test.client import Client


class TestEventsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('admin',
                                                  'admin@wizards.com',
                                                  'adminpass')

    def test_get_events_page(self):
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/events.html")

    def test_get_event_page(self):
        event = Event.objects.create()
        response = self.client.get(f'/events/{event.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/event.html")

    def test_get_add_event_page(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get('/events/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/add_event.html")

    def test_get_edit_event_page(self):
        self.client.login(username='admin', password='adminpass')
        event = Event.objects.create()
        response = self.client.get(f'/events/edit/{event.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "events/edit_event.html")

    def test_get_delete_event_page(self):
        self.client.login(username='admin', password='adminpass')
        event = Event.objects.create()
        response = self.client.get(f'/events/delete/{event.id}/')
        self.assertRedirects(response, '/events/')
        existing_events = Event.objects.filter(id=event.id)
        self.assertEqual(len(existing_events), 0)
