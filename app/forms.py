from django import forms
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighbourhood']
        
class UpdatesForm(forms.ModelForm):
    class Meta:
        model = Updates
        exclude = ['author','neighbourhood','post_date']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']