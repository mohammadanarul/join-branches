from django.urls import path
from .views import (
    PercelPicUpCreateView,
    PercelDeliveryCreateView,
    PicupAndDeliveryListView,
    PercelPicupList,
    PercelDeliveryList
)

app_name = 'percelpicupanddelivery'
urlpatterns = [
    path('picup-and-delivey-list/', PicupAndDeliveryListView.as_view(), name='picup_and_delivery_list'),
    path('picup-percel/', PercelPicupList.as_view(), name='picup_percel'),
    path('delivery-percel/', PercelDeliveryList.as_view(), name='delivery_percel'),
    path('percel-picup/', PercelPicUpCreateView.as_view(), name="percel_picup_view"),
    path('percel-delivery', PercelDeliveryCreateView.as_view(), name='percel_delivery_view'),
]