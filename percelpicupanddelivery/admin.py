from django.contrib import admin
from .models import PercelPicUpAndDelivery

@admin.register(PercelPicUpAndDelivery)
class PercelPicUpAndDeliveryModelAdmin(admin.ModelAdmin):
    pass
