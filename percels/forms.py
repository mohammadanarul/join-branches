from django import forms
from .models import Percel
from picuplocations.models import PicupLocation

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

'''
https://bdmidia.com/%e0%a6%a6%e0%a7%87%e0%a6%b6%e0%a7%87%e0%a6%b0-%e0%a6%96%e0%a6%ac%e0%a6%b0/%e0%a6%a8%e0%a6%bf%e0%a6%b0%e0%a7%8d%e0%a6%ae%e0%a6%be%e0%a6%a3-%e0%a6%b6%e0%a7%87%e0%a6%b7-%e0%a6%b9%e0%a6%93%e0%a7%9f%e0%a6%be%e0%a6%b0-%e0%a6%86%e0%a6%97%e0%a7%87%e0%a6%87-%e0%a6%ad/?fbclid=IwAR3kz0JcwPPemHPLljWwLRGOFMqB7YKbnAX56LkqURukZxdxcD_TORBxUO8
'''