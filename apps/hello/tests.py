# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.hello.models import Person


class IndexListTest(TestCase):
    """
    Add test for index page
    """
    fixtures = ['initial_data.json']

    def test_list_statuscode(self):
        """
        Test for main page
        """
        response = self.client.get(reverse('home'))
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, '42 Coffee Cups Test Assignment')
        self.assertTemplateUsed(response, 'hello/index.html')

    def test_1_user_in_db(self):
        """
        test for 1 user
        """
        self.assertEqual(Person.objects.count(), 1)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Babaiev')
        self.assertContains(response, '42 Coffee Cups Test Assignment')

    def test_none_user_in_db(self):
        """
        test none user in DB
        """
        Person.objects.all().delete()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The database contains no records')

    def test_2_user_in_db(self):
        """
        test 2 user in DB
        """
        self.person_two = Person.objects.create(
            name="Andy",
            surname="Tucker",
            date_of_birth="1907-08-01",
            other_contacts="The Gentle Graftery",
            bio="Jeff Peters as a Personal Magnet",
            email="andy.tuker@gmail.com",
            jabber="at@jabber.no",
            skype="andy.tucker",
        )

        self.assertEqual(Person.objects.count(), 2)
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, self.person_two.name, status_code=200)
        self.assertNotContains(response, self.person_two.surname)
