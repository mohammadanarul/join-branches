from django import forms
from .models import AreaLocation


class AreaLocationForm(forms.ModelForm):
    
    class Meta:
        model = AreaLocation
        fields = ("name", 'parent')
