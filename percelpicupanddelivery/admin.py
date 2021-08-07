from django.contrib import admin
from .models import PercelPicUp, PercelDelivery

@admin.register(PercelPicUp)
class PercelPicUpModelAdmin(admin.ModelAdmin):
    pass

@admin.register(PercelDelivery)
class PercelDeliveryModelAdmin(admin.ModelAdmin):
    pass
