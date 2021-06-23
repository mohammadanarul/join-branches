from django.contrib import admin
from .models import (
    Percel,
    PercelComplete,
    PercelProssesing,
)

@admin.register(Percel)
class PercelModelAdmin(admin.ModelAdmin):
    list_display        = ('percel_unique_id', 'customer_name', 'created_at', 'updated_at')
    list_filter         = ('percel_unique_id', 'created_at', 'is_active')
    readonly_fields     = ('percel_unique_id', 'created_at')


admin.site.register(PercelComplete)
admin.site.register(PercelProssesing)

# @admin.register(PercelPicUp)
# class PercelPicUpAdminModel(admin.ModelAdmin):
#     pass

# @admin.register(PercelDelivery)
# class PercelDeliveryAdminModel(admin.ModelAdmin):
#     pass
