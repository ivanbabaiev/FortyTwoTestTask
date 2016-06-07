# -*- coding: utf-8 -*-

from django.db import models


class Person(models.Model):
    """
    Create Person model
    """
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.CharField(max_length=50)
    jabber = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    other_contacts = models.TextField()

    def __unicode__(self):
        full_name = "%s %s" % (self.name, self.surname)
        return full_name


class Request(models.Model):
    """
    Create Requests model
    """
    date_time = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255)
    server_protocol = models.CharField(max_length=50)
    request_method = models.CharField(max_length=50)
    status_code = models.IntegerField(max_length=10)
    viewed = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_time']
