# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Request'
        db.create_table(u'hello_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('server_protocol', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status_code', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal(u'hello', ['Request'])


    def backwards(self, orm):
        # Deleting model 'Request'
        db.delete_table(u'hello_request')


    models = {
        u'hello.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hello.request': {
            'Meta': {'ordering': "['date_time']", 'object_name': 'Request'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['hello']