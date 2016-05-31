from django.contrib import admin

# Register your models here.

from .models import Person
from .models import Request


class AdminPersons(admin.ModelAdmin):
    """
    Persons model admin
    """
    list_display = ('name', 'surname', 'date_of_birth', 'bio', 'email',
                    'jabber', 'skype', 'other_contacts',)


class AdminRequest(admin.ModelAdmin):
    """
    Request model admin
    """
    list_display = ('id', 'date_time', 'path', 'server_protocol',
                    'request_method', 'status_code')


admin.site.register(Person, AdminPersons)
admin.site.register(Request, AdminRequest)
