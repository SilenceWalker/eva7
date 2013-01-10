from django.db import models
from django.contrib.auth.models import User

class Tech_Support(models.Model):
    tech_user = models.ForeignKey(User)
    
    def __unicode__(self):
        return unicode(self.tech_user)