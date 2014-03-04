# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Essay'
        db.create_table('pages_essay', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_edit_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('pages', ['Essay'])


    def backwards(self, orm):
        # Deleting model 'Essay'
        db.delete_table('pages_essay')


    models = {
        'pages.essay': {
            'Meta': {'object_name': 'Essay'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'last_edit_date': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['pages']