# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        pass

    def backwards(self, orm):
        # Deleting model 'Person'
        pass

    models = {

    }

    complete_apps = ['hello']
