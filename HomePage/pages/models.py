from django.db import models

class TextModel(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    publish_date = models.DateTimeField('Date Published')
    content = models.TextField(default='')
    rank = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Essay(TextModel):
    pass

class Biopic(TextModel):
    pass

class Personal(TextModel):
    pass
