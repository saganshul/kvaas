from django.db import models

class GetQuote(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    requirement = models.TextField()
    def __unicode__(self):
        return unicode(self.name)
