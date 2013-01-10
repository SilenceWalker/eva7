import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class TechUserForm(ModelForm):
    class Meta:
        model = User
        
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        
class TechForm(ModelForm):
    tech_user = forms.ModelChoiceField(required=False, queryset=User.objects.all(), help_text='Leave it blank')
    class Meta:
        model = models.Technical
        
        