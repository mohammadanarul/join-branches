from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import View, CreateView, ListView
from django.urls import reverse_lazy
from django.conf import settings
from accounts.views import StaffRequiredMixin
from .forms import PercelPicUpAndDeliveryForm

from .models import PercelPicUpAndDelivery

class PercelPicUpAndDeliveryCreateView(StaffRequiredMixin, CreateView):
    model = PercelPicUpAndDelivery
    template_name = 'percels/create_percel_picup_and_delivery.html'
    form_class = PercelPicUpAndDeliveryForm 
    success_url = reverse_lazy('percel:home_page')

