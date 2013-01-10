from django.db import models
from django.contrib.auth.models import User
from financial import models as finModels

class Technical(models.Model):
    tech_user = models.ForeignKey(User)
    coverage_area = models.ManyToManyField(finModels.Coverage_area)
    
    def __unicode__(self):
        return unicode(self.tech_user)