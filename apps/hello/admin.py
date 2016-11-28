from django.contrib import admin

# Register your models here.

from .models import Person, Request


class AdminPersons(admin.ModelAdmin):
    """
    Persons model admin
    """
    list_display = ('name', 'surname', 'date_of_birth', 'bio', 'email',
                    'jabber', 'skype', 'other_contacts',)

admin.site.register(Person, AdminPersons)
admin.site.register(Request)
