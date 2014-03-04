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
            ('publish_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2000, 1, 1, 0, 0))),
            ('content', self.gf('django.db.models.fields.TextField')(default='No Content Found')),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('pages', ['Essay'])

        # Adding model 'Biopic'
        db.create_table('pages_biopic', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('publish_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2000, 1, 1, 0, 0))),
            ('content', self.gf('django.db.models.fields.TextField')(default='No Content Found')),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('pages', ['Biopic'])

        # Adding model 'Personal'
        db.create_table('pages_personal', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('publish_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2000, 1, 1, 0, 0))),
            ('content', self.gf('django.db.models.fields.TextField')(default='No Content Found')),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('pages', ['Personal'])


    def backwards(self, orm):
        # Deleting model 'Essay'
        db.delete_table('pages_essay')

        # Deleting model 'Biopic'
        db.delete_table('pages_biopic')

        # Deleting model 'Personal'
        db.delete_table('pages_personal')


    models = {
        'pages.biopic': {
            'Meta': {'object_name': 'Biopic'},
            'content': ('django.db.models.fields.TextField', [], {'default': "'No Content Found'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        'pages.essay': {
            'Meta': {'object_name': 'Essay'},
            'content': ('django.db.models.fields.TextField', [], {'default': "'No Content Found'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        'pages.personal': {
            'Meta': {'object_name': 'Personal'},
            'content': ('django.db.models.fields.TextField', [], {'default': "'No Content Found'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2000, 1, 1, 0, 0)'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        }
    }

    complete_apps = ['pages']