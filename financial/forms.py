import models
from django import forms
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = models.User
        #exclude = ('username',)
        
class CoverageAreaForm(ModelForm):
    class Meta:
        model= models.Coverage_area