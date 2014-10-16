# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pregunta'
        db.create_table('system_pregunta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('system', ['Pregunta'])


    def backwards(self, orm):
        # Deleting model 'Pregunta'
        db.delete_table('system_pregunta')


    models = {
        'system.pregunta': {
            'Meta': {'object_name': 'Pregunta'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['system']