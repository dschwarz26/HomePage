from django.db import models

class Essay(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    publish_date = models.DateTimeField('Date Published')
    last_edit_date = models.DateTimeField('Last Edit Date')
    content = models.TextField(default='')

    def __unicode__(self):
        return self.name

class Biopic(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    publish_date = models.DateTimeField('Date Published')
    last_edit_date = models.DateTimeField('Last Edit Date')
    content = models.TextField(default='')

    def __unicode__(self):
        return self.name

class Personal(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    publish_date = models.DateTimeField('Date Published')
    last_edit_date = models.DateTimeField('Last Edit Date')
    content = models.TextField(default='')

    def __unicode__(self):
        return self.name
