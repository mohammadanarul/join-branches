from django.urls import path
from .views import (
    AreaLocationListview,
    AreaLocationCreateView
)

app_name = 'arealocations'
urlpatterns = [
    path('area-location-list/', AreaLocationListview.as_view(), name='area_location_list'),
    path('area-location-create/', AreaLocationCreateView.as_view(), name='create_arealocation_view'),
]