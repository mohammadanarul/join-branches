from django.contrib import admin
from .models import PicupLocation

@admin.register(PicupLocation)
class PicupLocationModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'picupname', 'picupaddress', 'picup_area', 'shop_phone_number']
    list_filter = ['created_at']
