# -*- coding: utf-8 -*-

from django.test import TestCase, Client

from apps.hello.models import Person


def create_person(st_name):
    """
    Create test Person
    """
    Person.objects.create(
        name=st_name,
        surname="Babaiev",
        date_of_birth="1971-12-23",
        other_contacts="https://ua.linkedin.com/in/ivanbabaiev",
        bio="Web developer",
        email="ivanbabaiev@gmail.com",
        jabber="ib@jabber.no",
        skype="ivan.babaiev",
    )


class IndexListTest(TestCase):
    """
    Add test for index page
    """
    def test_list_statuscode(self):
        """
        Test for status main page
        """
        create_person('')
        client = Client()
        response = client.get('/')
        self.failUnlessEqual(response.status_code, 200)

    def test_list_header(self):
        """
        Test for text on main page
        """
        create_person('')
        client = Client()
        response = client.get('/')
        self.assertContains(response, '42 Coffee Cups Test Assignment')

    def test_list_url_active(self):
        """
        Test on url active
        """
        create_person('')
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'hello/index.html')
