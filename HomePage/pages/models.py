from django.db import models
import datetime

class TextModel(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    publish_date = models.DateField('Date Published', default=datetime.date(2000,1,1))
    content = models.TextField(default='No Content Found')
    rank = models.IntegerField(default=-1)

    #TextModel is abstract, and db tables should not be created for it.
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

class Essay(TextModel):
    pass

class Biopic(TextModel):
    pass

class Personal(TextModel):
    pass
