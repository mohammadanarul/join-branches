from django import forms
from .models import (
    AreaLocation,
    PicupLocation,
    Percel,
    PercelPicUpAndDelivery
)


class AreaLocationForm(forms.ModelForm):
    
    class Meta:
        model = AreaLocation
        fields = ("name", 'parent')

class PicupLocationForm(forms.ModelForm):
    
    class Meta:
        model = PicupLocation
        fields = (
            "picupname",
            "picupaddress",
            "picup_area",
            "shop_phone_number",
            )

class PercelForm(forms.ModelForm):
    
    class Meta:
        model = Percel
        fields = (
            "picuplocation",
            "customer_name",
            "customer_phone_number",
            "customer_address",
            "product_weight",
            "area_location",
            "product_price",
            "customerdetails",
            )
        def __init__(self, user, *args, **kwargs):
            super(PercelForm, self).__init__(*args, **kwargs)
            self.fields['picuplocation'].queryset = PicupLocation.objects.filter(user=user)

class PercelPicUpAndDeliveryForm(forms.ModelForm):
    
    class Meta:
        model = PercelPicUpAndDelivery
        fields = (
            "pipuprider",
            "percel",
            "status"
            )
