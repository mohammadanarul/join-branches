from django.urls import path
from .views import (
    PicupLocationListview,
    PicupLocationCreateView,
)

app_name = 'picuplocations'
urlpatterns = [
    path('picuplocation-list/', PicupLocationListview.as_view(), name='picuplocation_list'),
    path('picup-location-create/', PicupLocationCreateView.as_view(), name="create_picuplocation_view"),
]