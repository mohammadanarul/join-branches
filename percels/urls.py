from django.urls import path
from .views import (
    home_page_view,
    AreaLocationCreateView,
    PicupLocationCreateView,
    percel_create_view,
    PercelPicUpAndDeliveryCreateView,
)

app_name = 'percels'
urlpatterns = [
    path('', home_page_view, name='home_page'),
    path('area-location-create/', AreaLocationCreateView.as_view(), name='arealocation_view'),
    path('picup-location-create/', PicupLocationCreateView.as_view(), name="picuplocation_view"),
    path('percel-create/', percel_create_view, name="percelcreate_view"),
    path('percelpicup-and-delivery/', PercelPicUpAndDeliveryCreateView.as_view(), name="percel_picup_and_delivery_view"),
]
