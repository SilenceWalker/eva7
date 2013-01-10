import models
from django import forms
from django.forms import ModelForm

class OSForm(ModelForm):
    class Meta:
        model = models.SO
        exclude = ('open_date','close_date','stats')