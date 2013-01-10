from django.db import models
from netControl import models as nC

class User(models.Model):
    username = models.CharField(max_length=64, unique=True, null=False, blank=False, default="", db_index=True)
    name = models.CharField(max_length=90, help_text="Please, the real name")
    cpf = models.CharField(max_length=15, verbose_name=u"CPF")
    rg = models.CharField(max_length=19, verbose_name=u"RG")
    address = models.CharField(max_length=35)
    address_number = models.IntegerField(max_length=5)
    city = models.ForeignKey("Coverage_area", blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'user'
    
class Coverage_area(models.Model):
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    def __unicode__(self):
        return self.city
    class Meta:
        db_table = 'coverage_area'