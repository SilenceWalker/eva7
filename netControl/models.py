from django.db import models

class radcheck(models.Model):
    username = models.CharField(max_length=64, null=False, blank=False, default="", db_index=True)
    attribute = models.CharField(max_length=64, null=False, blank=False, default="")
    op = models.CharField(max_length=2, null=False, blank=False, default="==")
    value = models.CharField(max_length=253, null=False, blank=False, default="")
    
    class Meta:
        db_table = 'radcheck'

class radgroupcheck(models.Model):
    groupname = models.CharField(max_length=64, null=False, blank=False, default="", db_index=True)
    attribute = models.CharField(max_length=64, null=False, blank=False, default="")
    op = models.CharField(max_length=2, null=False, blank=False, default="==")
    value = models.CharField(max_length=253, null=False, blank=False, default="")

class radgroupreply(models.Model):
    groupname = models.CharField(max_length=64, null=False, blank=False, default="", db_index=True)
    attribute = models.CharField(max_length=64, null=False, blank=False, default="")
    op = models.CharField(max_length=2, null=False, blank=False, default="=")
    value = models.CharField(max_length=253, null=False, blank=False, default="")

class radreply(models.Model):
    username = models.CharField(max_length=64, null=False, blank=False, default="", db_index=True)
    attribute = models.CharField(max_length=64, null=False, blank=False, default="")
    op = models.CharField(max_length=2, null=False, blank=False, default="=")
    value = models.CharField(max_length=253, null=False, blank=False, default="")

class radusergroup(models.Model):
    username = models.CharField(max_length=64, null=False, blank=False, default="", db_index=True)
    groupname = models.CharField(max_length=64, null=False, blank=False, default="")
    op = models.CharField(max_length=2, null=False, blank=False, default="=")
    value = models.CharField(max_length=253, null=False, blank=False, default="")

#class radpostauth(models.Model):
#    username = models.CharField(max_length=64, null=False, blank=False, default="")
#    pass = models.CharField(max_length=64, null=False, blank=False, default="")
#    reply = models.CharField(max_length=32, null=False, blank=False, default="")
#    authdate = models.DateTimeField(auto_now_add=True, null=False,) 