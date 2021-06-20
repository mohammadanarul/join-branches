from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import (
    PicupLocation,
    Percel,
    AreaLocation,
    PercelComplete,
    PercelProssesing,
    PercelPicUpAndDelivery
)

@admin.register(PicupLocation)
class PicupLocationModelAdmin(admin.ModelAdmin):
    pass

@admin.register(PercelPicUpAndDelivery)
class PercelPicUpAndDeliveryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Percel)
class PercelModelAdmin(admin.ModelAdmin):
    list_display        = ('percel_unique_id', 'customer_name', 'created_at', 'updated_at')
    list_filter         = ('percel_unique_id', 'created_at', 'is_active')
    readonly_fields     = ('percel_unique_id', 'created_at')

@admin.register(AreaLocation)
class LocationAdminModel(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = AreaLocation.objects.add_related_count(
                qs,
                Percel,
                'area_location',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = AreaLocation.objects.add_related_count(qs,
                 Percel,
                 'area_location',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

admin.site.register(PercelComplete)
admin.site.register(PercelProssesing)

# @admin.register(PercelPicUp)
# class PercelPicUpAdminModel(admin.ModelAdmin):
#     pass

# @admin.register(PercelDelivery)
# class PercelDeliveryAdminModel(admin.ModelAdmin):
#     pass
