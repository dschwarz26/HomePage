from django.db import models

class Essay(models.Model):
    name = models.CharField(max_length=200)
    publish_date = models.DateTimeField('Date Published')
    last_edit_date = models.DateTimeField('Last Edit Date')

    def __unicode__(self):
        return self.name
