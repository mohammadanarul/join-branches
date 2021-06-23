from django.urls import path
from .views import (
    HomeView,
    PercelListview,
    AreaLocationListview,
    PicupLocationListview,
    AreaLocationCreateView,
    PicupLocationCreateView,
    PercelCreateView,
    PercelPicUpAndDeliveryCreateView,
)

app_name = 'percels'
urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('percel-list/', PercelListview.as_view(), name='percels_list'),
    path('area-location-list/', AreaLocationListview.as_view(), name='area_location_list'),
    path('picuplocation-list/', PicupLocationListview.as_view(), name='picuplocation_list'),
    path('area-location-create/', AreaLocationCreateView.as_view(), name='arealocation_view'),
    path('picup-location-create/', PicupLocationCreateView.as_view(), name="create_picuplocation_view"),
    path('percel-create/', PercelCreateView.as_view(), name="percelcreate_view"),
    path('percelpicup-and-delivery/', PercelPicUpAndDeliveryCreateView.as_view(), name="percel_picup_and_delivery_view"),
]