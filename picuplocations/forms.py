from django import forms
from .models import PicupLocation

class PicupLocationForm(forms.ModelForm):
    
    class Meta:
        model = PicupLocation
        fields = (
            "picupname",
            "picupaddress",
            "picup_area",
            "shop_phone_number",
            )
