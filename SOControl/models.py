from django.db import models
from financial.models import User
from technical import models as tec

class SO(models.Model):
    client = models.ForeignKey(User)
    technical = models.ForeignKey(tec.Technical)
    description = models.TextField()
    open_date = models.DateTimeField(auto_now_add=True)
    stats = models.BooleanField()
    close_date = models.DateTimeField(auto_now_add=True)
