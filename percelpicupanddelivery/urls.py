from django.urls import path
from .views import (
    PercelPicUpAndDeliveryCreateView,
)

app_name = 'percelpicupanddelivery'
urlpatterns = [
    path('percelpicup-and-delivery/', PercelPicUpAndDeliveryCreateView.as_view(), name="percel_picup_and_delivery_view"),
]