from django.urls import path
from .views import (
    HomeView,
    PercelListview,
    PercelCreateView,
)

app_name = 'percels'
urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('percel-list/', PercelListview.as_view(), name='percels_list'),
    path('percel-create/', PercelCreateView.as_view(), name="percelcreate_view"),
]
