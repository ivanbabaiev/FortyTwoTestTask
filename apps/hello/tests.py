# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.hello.models import Person


class IndexListTest(TestCase):
    """
    Add test for index page
    """
    fixtures = ['initial_data.json']

    def setUp(self):
        self.person_two = Person.objects.create(
            name="Olla",
            surname="LLL",
            date_of_birth="1990-01-01",
            other_contacts="qwerty qwerty qwerty",
            bio="biography",
            email="google@google.com",
            jabber="xxx@jabber.org",
            skype="qwerty",
        )

    def test_list_statuscode(self):
        """
        Test for main page
        """
        response = self.client.get(reverse('home'))
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, '42 Coffee Cups Test Assignment')
        self.assertTemplateUsed(response, 'hello/index.html')

    def test_topic(self):
        """
        test 1 user in DB
        """
        response = Person.objects.get(pk=1)
        self.assertEqual(response.surname, 'Babaiev')

    def test_topic_1(self):
        """
        test none user in DB
        """
        Person.objects.all().delete()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The page you are looking'
                                      ' for could not be found.')

    def test_2_user(self):
        """
        test 2 user in DB
        """
        self.assertEqual(Person.objects.count(), 2)
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, self.person_two.name, status_code=200)
        self.assertNotContains(response, self.person_two.surname)
