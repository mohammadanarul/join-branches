from django import forms
from .models import PercelPicUp, PercelDelivery
from accounts.models import Rider


class PercelPicUpForm(forms.ModelForm):
    
    class Meta:
        model = PercelPicUp
        fields = (
            "pipup_rider",
            "percel",
            )
        
        def __init__(self, user=None, *args, **kwargs):
            # self.user = kwargs.pop('user', None)
            super(PercelPicUpForm, self).__init__(*args, **kwargs)
            self.fields['pipup_rider'].queryset = Rider.objects.filter(area_location=user.area_location)

class PercelDeliveryForm(forms.ModelForm):
    
    class Meta:
        model = PercelDelivery
        fields = (
            "delivery_rider",
            "picup_percel",
            )
        
        def __init__(self, user=None, *args, **kwargs):
            # self.user = kwargs.pop('user', None)
            super(PercelDeliveryForm, self).__init__(*args, **kwargs)
            self.fields['delivery_rider'].queryset = Rider.objects.filter(area_location=user.area_location)
